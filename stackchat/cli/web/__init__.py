"""
usage:
    stack.chat web [--read-only]
    stack.chat web --help
    stack.chat --help

Runs the local dev web server.
"""


import asyncio
import logging
import os

from aiohttp import web
import django.conf
import docopt

from . import urls


logger = logging.getLogger(__name__)


async def main(chat, opts):
    app = web.Application()

    if not django.conf.settings.configured:
        django.conf.settings.configure(DEBUG=True)

    def wrap_with_chat(f):
        return lambda *a, **kw: f(chat, *a, **kw)

    for route_pattern, f in urls.get_routes:
        app.router.add_get(route_pattern, wrap_with_chat(f))

    logger.info("Creating server.")
    server = await asyncio.get_event_loop().create_server(
        app.make_handler(), '0.0.0.0', int(os.environ.get('PORT') or 8080))

    logger.debug("Looping forever while server runs.")
    while True:
        # this might allow errors to pop up every interval?
        await asyncio.sleep(0.25)
