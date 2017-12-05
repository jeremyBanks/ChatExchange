import asyncio
import itertools
import asyncio
import logging
import os
import re
import html

from aitertools import alist, islice as aislice
from aiohttp import web



logger = logging.getLogger(__name__)


async def main(chat):
    app = web.Application()
    get = lambda route: lambda f: [app.router.add_get(route, f), f][-1]

    @get(r'/')
    async def index(request):
        return web.Response(content_type='text/html', text='''
            <!doctype html>
            <title>-m chatexchange web</title>
            <link rel="stylesheet" href="/style.css" />

            <p>servers: <a href="/se">Stack Exchange</a>, <a href="/so">Stack Overflow</a>, <a href="/mse">Meta Stack Exchange</a>
        ''')

    @get(r'/style.css')
    async def css(request):
        return web.Response(content_type='text/css', text='''
            body {
                font-family: monospace;
            }

            body {
                max-width: 800px;
                margin: 32px;
            }

            a {
                color: blue;
                text-decoration: underline;
                text-decoration-color: purple;
            }

                a:active {
                    color: red;
                }
        ''')

    @get(r'/{slug:[a-z]+}')
    async def server(request):
        slug = request.match_info['slug']
        server = chat.server(slug)

        html_name = html.escape("/%s %s (%s)" % (server.slug, server.name, server.host))
        html_info = html.escape(repr(dict(
           rooms=await server.rooms()
        )))

        return web.Response(content_type='text/html', text='''
            <!doctype html>
            <title>-m chatexchange web</title>
            <link rel="stylesheet" href="/style.css" />

            <h1>{html_name}</h1>

            <pre>{html_info}</pre>
        '''.format(**locals()))

    @get(r'/{slug:[a-z]+}/{room_id:[0-9]+}')
    async def room(request):
        slug = request.match_info['slug']
        room_id = int(request.match_info['room_id'])
        server = chat.server(slug)
        room = await server.room(room_id)
        messages = await alist(aislice(room.old_messages(), 0, 50))

        html_name = html.escape("/%s/%s#%s" % (server.slug, room.room_id, re.sub('[^a-z]+', '-', room.name.lower())))
        html_info = html.escape("\n".join(
            "%s: %s" % (m.owner.name, m.content_text or m.content_html or m.content_markdown) for m in messages
        ))

        return web.Response(content_type='text/html', text='''
            <!doctype html>
            <title>-m chatexchange web</title>
            <link rel="stylesheet" href="/style.css" />

            <h1>{html_name}</h1>

            <pre>{html_info}</pre>
        '''.format(**locals()))

    logger.info("Creating server.")
    server = await asyncio.get_event_loop().create_server(app.make_handler(), '127.0.0.1', 8080)

    logger.debug("Looping forever while server runs.")
    while True:
        # this might allow errors to pop up every interval?
        await asyncio.sleep(1.0)
