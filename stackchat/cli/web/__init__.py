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
import html
import logging
import os
import os.path
import re
import textwrap

from aitertools import alist, islice as aislice
from aiohttp import web
import django.template
import django.utils.html
import docopt

from ..._version import __version__


logger = logging.getLogger(__name__)


_templates = django.template.Engine(
    dirs=[
        os.path.join(os.path.dirname(__file__), 'templates'),
    ],
    debug=True,
    libraries={},
)


def render(template_name, context_data={}, content_type='text/html'):
    context_data = dict(context_data)
    context_data.setdefault('stackchat_version', __version__)
    context = django.template.Context(context_data)
    template = _templates.get_template(template_name)
    rendered = template.render(context)
    return web.Response(content_type=content_type, text=rendered)


async def main(chat, opts):
    app = web.Application()
    get = lambda route: lambda f: [app.router.add_get(route, f), f][-1]

    @get(r'/')
    async def index(request):
        # handle explicit oneboxing as image with `!https://stack.chat`
        if request.headers.getall('ACCEPT', [''])[0].lower().startswith('image/'):
            s = "stack.chat version %s" % (__version__)

            lines = textwrap.wrap(s, width=42, subsequent_indent='  ')[:16]

            height = 18 * len(lines)

            parts = [
                '<?xml version="1.0" encoding="utf-8"?>'
                '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="full"'
                    ' width="300" height="%s">'
                '<style>text{'
                    'fill:black;'
                    'stroke:#fbf2d9;'
                    'font-size:12px;'
                    'font-family:Consolas,monospace;'
                '}</style>' % (height)
            ]

            for i, line in enumerate(lines):
                y = 15 + 18 * i
                h = html.escape(line)
                parts.append(
                    '<text x="0" y="%s" text-anchor="start" style="stroke-width:2px;">%s</text>'
                    '<text x="0" y="%s" text-anchor="start" style="stroke-width:0;">%s</text>' % (y, h, y, h)
                )

            parts.append('</svg>')

            return web.Response(content_type='image/svg+xml', text=''.join(parts))

        return render('index.html')

    @get(r'/style.css')
    async def css(request):
        return render('style.css', content_type='text/css')

    @get(r'/{slug:[a-z]+}')
    async def server(request):
        slug = request.match_info['slug']
        server = chat.server(slug)

        html_name = html.escape("server = chat.server(%r) # %s" % (server.slug, server.name))
        html_info = "\n".join(
           ("<p><a href=\"%s\">server.room(%s) # %s</a></p>" % (html.escape("/%s/%s" % (slug, room.room_id)), room.room_id, html.escape(room.name))) for room in await server.rooms())

        return render('server.html', {
            'html_name': django.utils.html.mark_safe(html_name),
            'html_info': django.utils.html.mark_safe(html_info),
        })

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
        return render('room.html', {
            'html_name': django.utils.html.mark_safe(html_name),
            'html_messages': django.utils.html.mark_safe(html_messages),
        })

        return web.Response('room.html')

    logger.info("Creating server.")
    server = await asyncio.get_event_loop().create_server(app.make_handler(), '0.0.0.0', int(os.environ.get('PORT') or 8080))

    logger.debug("Looping forever while server runs.")
    while True:
        # this might allow errors to pop up every interval?
        await asyncio.sleep(1.0)
