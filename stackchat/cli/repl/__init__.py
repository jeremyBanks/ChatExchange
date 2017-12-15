"""
usage:
    stack.chat repl
    stack.chat repl --help
    stack.chat --help

Opens a Python REPL with an instantitated chat Client.
"""


import asyncio
import code
import readline
import sys
import time

from ..._version import __version__


def main(chat, opts):
    readline.parse_and_bind('"\C-r": reverse-search-history')
    readline.parse_and_bind('"\C-s": forward-search-history')

    loop = asyncio.get_event_loop()

    def await_(coro):
        return loop.run_until_complete(asyncio.ensure_future(future))
    await_.__name__ = 'await'

    return code.interact(
        local={
            'chat': chat,
            'await': await_,
        },
        banner=
            f'# Python {sys.version}\n'
            f'# stack.chat version {__version__}\n'
            f'await = lambda coro: …\n'
            f'with stackchat.Client(…) as chat:',
        exitmsg='',
    )
