"""
usage:
    stack.chat tail [-n=N] [-f] SERVER ROOM_ID
    stack.chat tail --help
    stack.chat --help

Displays the latest messages in a chat room, optionally watching for more.

command options:
    --num, -n     Number of recent messages to show. [default: 10]
    --follow, -f
"""


import asyncio
import logging

import docopt

import stackchat



logger = logging.getLogger(__name__)


async def main(chat, argv):
    opts = docopt.docopt(__doc__.replace('stack.chat', argv[0]), argv[1:], True)
    logger.debug("subcommand optparse opts: %s" % opts)

    server_slug = opts['SERVER']
    room_id = int(opts['ROOM_ID'])

    old_limit = int(opts['--num'])

    server = chat.server(server_slug)
    room = await server.room(room_id)

    print("ROOM NAME: ", room.name)

    n = 0
    async for m in room.old_messages():
        n += 1
        print(m.message_id, '[', m.owner and m.owner.name, ']', (m.content_text or m.content_html)[:64])

        if n >= old_limit: 
            break

    print('#---')

    if opts['--follow']:
        async for m in room.new_messages():
            n += 1
            print(m.message_id, '[', m.owner and m.owner.name, ']', (m.content_text or m.content_html)[:64])

        return
