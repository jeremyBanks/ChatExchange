"""
usage:
    stack.chat web
    stack.chat web --help
    stack.chat --help

Runs the local dev web server.
"""


import asyncio
import itertools
import asyncio
import logging
import os
import re
import html

from aitertools import alist, islice as aislice
from aiohttp import web
import docopt



logger = logging.getLogger(__name__)


async def main(chat, opts):
    app = web.Application()
    get = lambda route: lambda f: [app.router.add_get(route, f), f][-1]

    @get(r'/')
    async def index(request):
        return web.Response(content_type='text/html', text=r'''
            <!doctype html>
            <title>-m stackchat web</title>
            <link rel="stylesheet" href="/style.css" />

            <p>
                import stackchat
            </p>

            <h1>with stackchat.Client(...) as chat:</h1>

            <p><a href="/se">chat.server("se") # Stack Exchange</a></p>
            <p><a href="/so">chat.server("so") # Stack Overflow</a></p>
            <p><a href="/mse">chat.server("mse") # Meta Stack Exchange</a></p>
        ''')

    @get(r'/style.css')
    async def css(request):
        return web.Response(content_type='text/css', text=r'''
            body {
                font-family: monospace;
            }

            * {
                font-family: inherit;
            }

            body {
                max-width: 800px;
                margin: 32px;
                padding-left: 32px;
            }

            h1 {
                margin: 0;
                margin-top: 16px;
                margin-left: -32px; 
            }

            h2 {
                margin: 0;
                margin-top: 8px;
                margin-left: -16px; 
            }

            h3 {
                margin: 0;
                margin-top: 4px;
                margin-left: -8px; 
            }

            h4 {
                margin: 0;
                margin-top: 2px;
                margin-left: -4px; 
            }

            a {
                color: blue;
                text-decoration: underline;
                text-decoration-color: purple;
            }

                a:active {
                    color: red;
                }

            input {
                border: none;
                background: none;
                width: 256px;
            }

            button {
                font-weight: bold;
            }
        ''')

    @get(r'/{slug:[a-z]+}')
    async def server(request):
        slug = request.match_info['slug']
        server = chat.server(slug)

        html_name = html.escape("server = chat.server(%r) # %s" % (server.slug, server.name))
        html_info = "\n".join(
           ("<p><a href=\"%s\">server.room(%s) # %s</a></p>" % (html.escape("/%s/%s" % (slug, room.room_id)), room.room_id, html.escape(room.name))) for room in await server.rooms())

        return web.Response(content_type='text/html', text=r'''
            <!doctype html>
            <title>-m stackchat web</title>
            <link rel="stylesheet" href="/style.css" />

            <p>
                import stackchat
            </p>

            <h1>with stackchat.Client(...) as chat:</h1>

            <h2>{html_name}</h2>

            {html_info}
        '''.format(**locals()))

    @get(r'/{slug:[a-z]+}/{room_id:[0-9]+}')
    async def room(request):
        slug = request.match_info['slug']
        room_id = int(request.match_info['room_id'])
        server = chat.server(slug)
        room = await server.room(room_id)
        messages = await alist(aislice(room.old_messages(), 0, 5))

        html_name = html.escape("room = await chat.server(%r).room(%r) # %s" % (server.slug, room.room_id, room.name))
        html_messages = "\n".join(
            "<b><a href=\"/u/%s\">%s</a></b>: %s" % (m.owner.user_id, html.escape(m.owner.name), html.escape(m.content_text or m.content_html or m.content_markdown)) for m in messages
        )

        return web.Response(content_type='text/html', text=r'''
            <!doctype html>
            <title>-m stackchat web</title>
            <link rel="stylesheet" href="/style.css" />

            <p>
                import stackchat<br />
                from aitertools import alist, islice as aislice
            </p>

            <h1>with stackchat.Client(…) as chat:</h1>

            <h2>{html_name}</h2>

            <h3>room.send(</h3>

            <form method="POST">
                "<input name="content_markdown" placeholder="Hello, world." />"<button type="submit">) # send</button>
            </form>

            <h3>messages = await alist(aislice(room.old_messages(), 0, 5))</h3>

            <pre>{html_messages}</pre>

            <h3>async for message in aislice(room.new_messages(), 0, 5):</h3>

            <pre>NotImplemented</pre>
        '''.format(**locals()))

    logger.info("Creating server.")
    server = await asyncio.get_event_loop().create_server(app.make_handler(), '0.0.0.0', int(os.environ.get('PORT') or 8080))

    logger.debug("Looping forever while server runs.")
    while True:
        # this might allow errors to pop up every interval?
        await asyncio.sleep(1.0)
