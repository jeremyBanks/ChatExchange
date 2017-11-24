import asyncio
import logging

from pprintpp import pprint

import chatexchange



async def main():
    logging.getLogger('').setLevel(logging.ERROR)
    logging.getLogger('chatexchange').setLevel(logging.INFO)

    server_slug = 'se'
    room_id = 2110

    with chatexchange.Client() as chat:
        server = chat.server(server_slug)
        room = await server.room(room_id)

        pprint(room.name)
        async for m in room.old_messages():
            pprint({m.owner and m.owner.name: m.content_text or m.content_html[:72]})

    return
