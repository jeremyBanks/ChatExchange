import asyncio
import logging

import stackchat



async def main(chat, server_slug='se', room_id='1', content_markdown="hello, world"):
    server = chat.server(server_slug)
    room = await server.room(room_id)
    room.send(content_markdown)
