import asyncio

import chatexchange



async def main():
    server_slug = 'se'
    room_id = 2110

    with chatexchange.Client() as chat:
        server = chat.server(server_slug)
        room = await server.room(room_id)

        print(room)

    return
