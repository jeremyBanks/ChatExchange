"""
usage:
    stack.chat repl
    stack.chat repl --help
    stack.chat --help

Opens a Python REPL with an instantiated instance.
"""


import asyncio
import code
import sys

from ..._version import __version__


async def main(chat, opts):
    def await_(future):
        return asyncio.get_event_loop().run_until_complete(future)
    await_.__name__ = 'await'

    return code.interact(
        local={
            'chat': chat,
            'await': await_,
        },
        banner=
            f'# Python {sys.version}\n'
            f'# stack.chat version {__version__}\n'
            f'await = lambda future: …\n'
            f'with stackchat.Client(…) as chat:',
        exitmsg='',
    )
