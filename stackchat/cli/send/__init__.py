"""
usage:
    stack.chat send SERVER ROOM_ID [--] [MESSAGES...]
    stack.chat send SERVER ROOM_ID
    stack.chat send --help
    stack.chat --help

Sends one or more messages, specified as arguments or read from stdin.
"""


import asyncio
import logging

import docopt



logger = logging.getLogger(__name__)


async def main(chat, argv):
    opts = docopt.docopt(__doc__.replace('stack.chat', argv[0]), argv[1:], True)
    logger.debug("subcommand optparse opts: %s" % opts)

    server = chat.server(opts['SERVER'])
    room_id = int(opts['ROOM_ID'])
    room = await server.room(room_id)
    logger.info(room)

    messages = opts['MESSAGES']
    if messages:
        for message in messages:
            await room.send(message)
    else:
        while True:
            message = input('> ').strip()
            if message:
               await room.send(message)
            else:
                break
