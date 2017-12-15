import datetime
import textwrap
import html
import mimetypes
import os.path

from aitertools import alist, islice as aislice
from aiohttp import web
import django.template
import django.utils.html

from ..._version import __version__


_get_routes = []


_init_datetime = datetime.datetime.utcnow().replace(microsecond=0)


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


def render(template_name, context_data={}, content_type=None):
    if content_type == None:
        content_type, _  = mimetypes.guess_type(template_name, strict=False)

    if content_type == None:
        content_type = 'text/plain'

    context_data = dict(context_data)
    context_data.setdefault('stackchat_version', __version__)
    context = django.template.Context(context_data)
    template = _templates.get_template(template_name)
    rendered = template.render(context)
    return web.Response(content_type=content_type, text=rendered)


@_get(r'/')
async def index(chat, request):
    # handle explicit oneboxing as image
    if request.headers.getall('ACCEPT', [''])[0].lower().startswith('image/'):
        lines = [
            f'!{(request.forwarded and request.forwarded[0]["proto"]) or request.scheme}://{request.host}',
            f'# stack.chat version {__version__}',
            f'# up since {_init_datetime.isoformat()}Z'
        ]

        total_width_px = 300
        line_height_px = 18
        text_width_chars = 42
        text_height_chars = 16

        lines = ('\n'.join(textwrap.fill(
            line,
            replace_whitespace=False,
            drop_whitespace=False,
            width=text_width_chars,
            subsequent_indent='  '
        ) for line in lines)).split('\n')
        
        lines = lines[:text_height_chars]

        return render('index.svg', {
            'width': total_width_px,
            'height': 18 * len(lines),
            'lines': [{
                'y': 15 + 18 * i,
                'text': text
            } for i, text in enumerate(lines)]
        })

    return render('index.html')


@_get(r'/style.css')
async def css(chat, request):
    return render('style.css')


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
