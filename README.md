# This README is more aspirational than descriptive, that is to say, this is mostly `NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED NOT IMPLEMENTED`.

ChatExchange 3
==============

A Python 3 library and command-line tool for Stack Exchange chat.

## Installation

```
pip install chatexchange3  # or your Python 3 packaging alternative of choice
```

## Authentication

For authenticated use specify a Stack Exchange username and password in
the `ChatExchangeU` and `ChatExchangeP` environment variables. OpenID and
OAuth authentication are not supported.

## Command-Line Interface

This hasn't been implemented, but I'd like to support things like this.

### Examples

Import (or update) the full history of a chatroom to the database.
Records updated within the last 3600 seconds will be considered up-to-date.

```
chatexchange sqlite://./data se/r/1 --all --max-age=3600
```

Add new messages to the database as they come in:

```
chatexchange sqlite://./data chat.stackexchange.com/rooms/1 --all --max-age=Infinity --watch
```

Send a message, then disconnect (a temporary in-memory SQLite database will be used):

```
chatexchange se/r/1 --send "hello world"
```

Or maybe using our local slugs:

```
chatexchange r/B6 -s "hello world"
```

## Python Interface

### Public (Please Use)

The root of the interface is your `Client`, either `BlockingClient`:

```
chat = chatexchange.BlockingClient(auth=('em@i.l', 'p4ssW0rd'))
sandbox = chat.se.room(room_id=1)
hello = sandbox.send("hello, %s 😶" % (room.name))
for i, reply in enumerate(hello.replies()):
    if i == 0:
        reply.reply("hello, %s. 😐" % (reply.name))
    elif i == 1:
        reply.reply("Hello, %s. 🙂" % (reply.name))
    else:
        reply.reply("Hello, %s! 😄" % (reply.name))
        break

time.sleep(1.0)
goodbye = sandbox.send("see y'all later!")
```

or `AsyncClient`:

```
chat = chatexchange.AsyncClient(auth=('em@i.l', 'p4ssW0rd'))
sandbox = await chat.se.room(room_id=1)
hello = await sandbox.send("hello, %s 😶" % (room.name))
async for i, reply in chatexchange.async.enumerate(hello.replies()):
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

Here's most of the API:

```
- chatexchange
    - .AsyncClient(db_path='sqlite:///:memory:', auth=None)
        - .server(slug) -> .client.Server
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
            @classmethod .meta_id_from_meta_slug(meta_slug) -> int
        - .Server extends .Base
            - .url: str
            - .slug: str
            - .name: strstr
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
            - async .user(id) -> .User()
            - async .room(id) -> .Room()
            - async .message(id) -> .Message()
            - async .rooms() # all rooms from most-recently-active to least
            - async .me() -> User() | None
            - async .favorite_rooms()
        - .User extends ..models.User
            - .server -> .Server
            - async .messages(from=EPOCH)
            - infinite async .new_messages(to=SUNSET)
            - infinite async .all_messages(from=EPOCH, to=SUNSET)
        - .Room extends ..models.Room
            - .server -> .Server
            - async .send(content_markdown)
            - async .ping(user, content_markdown)
            - async .messages(from=EPOCH)
            - infinite async .new_message(to=SUNSET)
            - infinite async .all_messages(from=EPOCH, to=SUNSET)
        - .Message extends ..models.Message
            - .owner -> .User
            - .room -> .Room
            - async .reply(content_markdown) -> Message
            - async .edit(content_markdown) -> None
            - async .replies(from=EPOCH)
            - infinite async .new_replies(to=SUNSET)
            - infinite async .all_replies(from=EPOCH, to=SUNSET)
    - .async # generic async utils, don't really belong, but might be useful
```

### Internal (Do Not Use)

```
- chatexchange
    - ._seed
        - .data() # yields a bunch of seed data that needs to be added to new databases
    - ._parser # classes interpreting specific HTML pages as structured data
        - .TranscriptPage
    - ._obj_dict
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
https://github.com/jeremyBanks/ChatExchange/contributors and
https://github.com/Manishearth/ChatExchange/contributors.
