import asyncio
import logging

import chatexchange



async def main(chat):
    logging.getLogger('').setLevel(logging.DEBUG)
    logging.getLogger('chatexchange').setLevel(logging.DEBUG)

    server_slug = 'so'
    room_id = 1

    old_limit = 10
    new_limit = 2

    server = chat.server(server_slug)
    room = await server.room(room_id)

    print("ROOM NAME: ", room.name)

    n = 0
    async for m in room.old_messages():
        n += 1
        print(m.message_id, '[', m.owner and m.owner.name, ']', (m.content_text or m.content_html)[:64])

        if n >= old_limit: 
            break

    n = 0
    async for m in room.new_messages():
        n += 1
        print(m.message_id, '[', m.owner and m.owner.name, ']', (m.content_text or m.content_html)[:64])

        if n >= new_limit:
            break

    return
