# This README is more aspirational than descriptive, that is to say, this is mostly `NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED`.

stack.chat
==========

A Python 3 library and command-line tool for Stack Exchange chat.

## Installation

```
pip install stack.chat  # or your Python 3 packaging alternative of choice
```

## Authentication

For authenticated use specify a Stack Exchange email address and password in
the `STACK_EXCHANGE_EMAIL` and `STACK_EXCHANGE_PASSWORD` environment variables.
OpenID and OAuth authentication are not supported.

### Examples

Import (or update) the full history of a chatroom to the database.
Records updated within the last 3600 seconds will be considered up-to-date.

```
stack.chat sqlite://./data se/r/1 --all --max-age=3600
```

Add new messages to the database as they come in:

```
stack.chat sqlite://./data chat.stackexchange.com/rooms/1 --all --max-age=Infinity --watch
```

Send a message, then disconnect (a temporary in-memory SQLite database will be used):

```
stack.chat se/r/1 --send "hello world"
```

Or maybe using our local slugs:

```
stack.chat r/B6 -s "hello world"
```

## Python Interface

### Public (Please Use)

The root of the interface is your `Client`:

```
chat = stackchat.Client(auth=('em@i.l', 'p4ssW0rd'))
sandbox = await chat.se.room(room_id=1)
hello = await sandbox.send("hello, %s 😶" % (room.name))
async for i, reply in stackchat.async.enumerate(hello.replies()):
    if i == 0:
        reply.reply("hello, %s. 😐" % (reply.name))
    elif i == 1:
        reply.reply("Hello, %s. 🙂" % (reply.name))
    else:
        reply.reply("Hello, %s! 😄" % (reply.name))
        break

await asyncio.sleep(1.0)
goodbye = await sandbox.send("see y'all later!")
```

Lots of methods will take `desired_max_age=` and `required_max_age=` parameters.
If a local result is available that has been updated within the desired number
of seconds, it will be returned immediately. If not, we'll try to request a remote
result. If that fails, but we have a local result updated within the required
number of seconds, return that and log a warning, else raise an error.

There's also an `offline=True` option to use only local data.

Here's most of the API:

```
- stackchat
    - .Client(db_path='sqlite:///:memory:', auth=None)
        - .server(slug_or_host) -> .client.Server
        - .se -> .client.Server
        - .so -> .client.Server
        - .mse -> .client.Server
        - .sql_engine -> SQLAlchemy Engine
        - .sql_session() -> SQLAlchemy Session Bound to Engine
        - some caching settings too

    - .models # SQLAlchmeny models for the data 
        - .Base(**attrs) extends SQLAlchemy ORM Declarative Base
            - .__repr__
            - .set(**attrs) -> self
            - .meta_id: int
            - .meta_created: DateTime
            - .meta_updated: DateTime
            - .meta_deleted: DateTime
            - .deleted: boolean
            - .meta_slug: str
            - @classmethod .meta_id_from_meta_slug(meta_slug) -> int

        - .Server extends .Base
            - .url: str
            - .slug: str
            - .name: str

        - .User extends .Base
            - .server_meta_id: int
            - .id: int
            - .name: str

        - .Room extends .Base
            - .server_meta_id: int
            - .id: int
            - .name: str

        - .Message extends .Base
            - .owner_meta_id: int
            - .room_meta_id: int
            - .id: int
            - .content_html: str
            - .content_text: str # derived from the HTML
            - .content_markdown: str # usually None because we don't know it

    - .client # Extended models with a reference to the client and lots of sugar
        - .Server extends ..models.Server
            - async .user(id, **cache_opts) -> .User()
            - async .room(id, **cache_opts) -> .Room()
            - async .message(id, **cache_opts) -> .Message()
            - async .rooms(**cache_opts) # all rooms from most-recently-active to least
            - async .me(**cache_opts) -> User() | None
            - async .me_replies(**cache_opts)
            - async .favorite_rooms(**cache_opts)
            - async .search(q, owner_id, room_id)

        - .User extends ..models.User
            - .server -> .Server
            - async .messages(from=EPOCH, **cache_opts)

        - .Room extends ..models.Room
            - .server -> .Server
            - async .send(content_markdown)
            - async .ping(user, content_markdown)
            - async .messages(from=EPOCH, **cache_opts)
            - infinite async .new_message(to=SUNSET)
            - infinite async .all_messages(from=EPOCH, to=SUNSET, **cache_opts)

        - .Message extends ..models.Message
            - .owner -> .User
            - .room -> .Room
            - async .reply(content_markdown) -> Message
            - async .edit(content_markdown) -> None
            - async .replies(from=EPOCH, **cache_opts)
            - infinite async .new_replies(to=SUNSET)
            - infinite async .all_replies(from=EPOCH, to=SUNSET, **cache_opts)

    - .async # generic async utils, don't really belong, but might be useful
```

### Internal (Do Not Use)

```
- stackchat
    - ._seed
        - .data() # yields a bunch of seed data that needs to be added to new databases

    - .scraper # classes interpreting specific HTML pages as structured data
        - .TranscriptDay

    - .obj_dict
        - .update(o, **attrs) # a generic __init__ asserting named attributes already exist 
        - .updated(o, **attrs) # chainable version of .update()
        - .repr(o) -> # a generic __repr__() useful for debugging
```

## License

Licensed under either of

 - Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or
   http://www.apache.org/licenses/LICENSE-2.0)
 - MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.

### Contributors

Please see the Git commit history or 
https://github.com/Manishearth/stackchat/contributors and
https://gitlab.com/stack.chat/stack.chat/graphs/master.
