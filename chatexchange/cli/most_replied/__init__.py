import asyncio
import itertools
import logging
import os

from pprintpp import pprint as print

from chatexchange.client import Client



logger = logging.getLogger(__name__)


async def main(chat):
    rooms = [
        chat.mse.room(89),
        chat.se.room(11540),
        chat.so.room(6)
    ]

    for room in await asyncio.gather(*rooms):
        async for message in room.old_messages():
            pass

        await report_most_replied(chat, room.server, room)


async def report_most_replied(chat, server, room):
    with chat.sql_session() as sql:
        most_replied_to_ids = [id for (id,) in itertools.islice(sql.execute('''
                select
                    message.parent_message_id as message_id
                from
                    Message message
                    left join Room room on message.room_meta_id = room.meta_id
                    left join Server server on message.server_meta_id = server.meta_id
                    left join Message parent on message.parent_message_id = parent.message_id and message.server_meta_id = parent.server_meta_id
                where
                    server.meta_id = :server_meta_id
                    and room.room_id = :room_id
                group by
                    message.parent_message_id
                order by
                    count(message.parent_message_id) desc
        ''', {'server_meta_id': room.server_meta_id, 'room_id': room.room_id}), 4)]

    print("Most replied-to messages in room #%s: %s:" % (room.room_id, room.name))
    for message_id in most_replied_to_ids:
        message = await server.message(message_id)
        replies = await message.replies()
        print("%s replies (%s)" % (len(replies), ", ".join("%s by %s" % (m.message_id, m.owner.name) for m in replies)))
        print("https://%s/transcript/message/%s" % (server.host, message.message_id))
