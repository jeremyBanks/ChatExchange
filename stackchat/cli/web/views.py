from aitertools import alist, islice as aislice
import textwrap
import html
import os.path

from aiohttp import web
import django.template
import django.utils.html

from ..._version import __version__


_get_routes = []


def _get(route_pattern):
    def decorate(f):
        _get_routes.append((route_pattern, f))
        return f
    return decorate


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


@_get(r'/')
async def index(chat, request):
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


@_get(r'/style.css')
async def css(chat, request):
    return render('style.css', content_type='text/css')


@_get(r'/{slug:[a-z]+}')
async def server(chat, request):
    slug = request.match_info['slug']
    server = chat.server(slug)

    html_name = html.escape("server = chat.server(%r) # %s" % (server.slug, server.name))
    html_info = "\n".join(
        ("<p><a href=\"%s\">server.room(%s) # %s</a></p>" % (html.escape("/%s/%s" % (slug, room.room_id)), room.room_id, html.escape(room.name))) for room in await server.rooms())

    return render('server.html', {
        'html_name': django.utils.html.mark_safe(html_name),
        'html_info': django.utils.html.mark_safe(html_info),
    })


@_get(r'/{slug:[a-z]+}/{room_id:[0-9]+}')
async def room(chat, request):
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
