import asyncio
import itertools
import asyncio
import logging
import os

from aiohttp import web



logger = logging.getLogger(__name__)


async def main(chat):
    app = web.Application()
    get = lambda route: lambda f: [app.router.add_get('/', f), f][-1]

    @get('/')
    async def index(self):
        return web.Response(content_type='text/html', text='''<!doctype html>
            <h1><code>python3 -m chatexchange web</code></h1>

            <p>
                <code>NotImplementedError</code> <code>;)</code>
            </p>
        ''')

    logger.info("Creating server.")
    server = await asyncio.get_event_loop().create_server(app.make_handler(), '127.0.0.1', 8080)

    logger.debug("Looping forever while server runs.")
    while True:
        # this might allow errors to pop up every two seconds?
        await asyncio.sleep(1.0)
