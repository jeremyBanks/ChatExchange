import asyncio

import chatexchange



async def main():
    server_slug = 'se'
    room_id = 2110

    with chatexchange.Client() as chat:
        server = chat.server(server_slug)
        room = await server.room(room_id)

        print(room.name)
        n = 0
        async for m in room.old_messages():
            n += 1
            if n > 10:
                break
            print(m.content_text or m.content_html)

    return
