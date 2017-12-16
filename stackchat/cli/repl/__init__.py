"""
usage:
    stack.chat repl
    stack.chat repl --help
    stack.chat --help

Opens a Python REPL with an instantitated chat Client.
"""


import asyncio
import code
import sys
import textwrap
import time

from ..._version import __version__


def dedent(s):
    common_prefix = None
    lines = s.split('\n')

    whitespace_chars = set(' \t')

    for line in lines:
        if all(c in whitespace_chars for c in line):
            continue
        elif common_prefix is None:
            common_prefix = ''
            for char in line:
                if char in whitespace_chars:
                    common_prefix += char
                else:
                    break
            if common_prefix == '': return s
        else:
            if len(line) < len(common_prefix):
                common_prefix = common_prefix[:len(line)]
                if common_prefix == '': return s

            for i, (current, expected) in enumerate(zip(line, common_prefix)):
                if current != expected:
                    common_prefix = common_prefix[:i]
                    break

    return '\n'.join(line[len(common_prefix):] for line in lines)



def main(chat, opts):
    loop = asyncio.get_event_loop()

    await = lambda coro: asyncio.get_event_loop().run_until_complete(coro)

    console = code.InteractiveConsole({'chat': chat})

    init_code = dedent(rf'''
        # Python {textwrap.fill(sys.version, subsequent_indent='        #        ')}
        # stack.chat version {__version__}

        import asyncio
        import stackchat

        # shortcut for running coroutines from REPL 
        await = lambda coro: asyncio.get_event_loop().run_until_complete(coro)
    ''').strip('\n')

    init_pseudocode = dedent(r'''
        with stackchat.Client(…) as chat:
        >>> chat.se.name, chat.so.name, chat.mse.name
    ''').strip('\n')

    for line in init_code.split('\n'):
        sys.stderr.write(line + '\n')
        console.push(line)

    sys.stderr.write('\n')

    for line in init_pseudocode.split('\n'):
        sys.stderr.write(line + '\n')

    console.push('chat.se.name, chat.so.name, chat.mse.name')
    sys.stderr.write('>>> \n')

    return console.interact(banner=f'', exitmsg='')
