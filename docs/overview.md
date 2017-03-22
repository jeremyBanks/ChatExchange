# ChatExchange Overview

[ChatExchange] provides an unofficial object-oriented API for interacting with [Stack Exchange chat][chat.se] from Python. This document provides an overview and examples of ChatExchange's capabilities.

You may also be interested in [our auto-generated epydocs][epydocs], but note that they still include many things that are depreacted or only meant for internal use.

## Installation

### From PyPI

Releases are available on PyPI as `ChatExchange`.

    pip install ChatExchange

### From Source

From a downloaded/cloned copy of the ChatExchange source code, you can install it and its dependencies in your local Python environment by running:

    pip install -e .

If you have the source you'll also have our `./repl` script available. It launches a BPython REPL, imports ChatExchange, and grabs a few objects from the API. It's a good way to quickly jump in to experiment with the API. (You can set the `ChatExchangeU` and `ChatExchangeP` environment variables instead of being prompted to authenticate every time.)

## `chatexchange.Client`

`chatexchange.Client` is the top-level class that manages your connections to a Stack Exchange Chat network. All other data and functionality can be accessed by starting from a `Client` instance.

```python
import chatexchange

host = 'stackexchange.com'
email = 'chatexchange@example.com'
password = 'aS0N6iS4WtheOC34Nsing'

with chatexchange.Client(host, email, password) as chat:
    sandbox = chat.get_room(1)
    sandbox.send_message("hello, world")
```

A client can optionally be authenticated as a specific user by providing their [Stack Exchange OpenID] email address and password.

There are three possible Stack Exchange Chat `host`s: `chat.stackexchange.com`, `chat.stackoverflow.com`, and `chat.meta.stackexchange.com`.

### Methods

- `.login(str, str)` Can be used to authenticate with an email address and password, if they weren't already provided to the constructor.
- `.logout()` Cleans up all resources (connections, threads) used by the Client. This will be automatically called if you use a `with` statement for the Client.
- `.get_room(int):Room` Returns the Room with a given ID.
- `.get_user(int):User` Returns the User with a given ID.
- `.get_message(int):Message` Returns the Message with a given ID.
- `.get_me():User` Returns the currently-authenticated User.


## Common Object Behaviours

The `Room`, `User`, and `Message` classes share some important behaviours to note up-front.

**Except for `.id`, most of their properties are "lazy".** The values will only be fetched from the network the first time they're accessed, so exceptions could occur at that time.

```python
with chatexchange.Client(host, email, password) as chat:
    sandbox = chat.get_room(1)

    # When we access one of these properties it makes a network request
    # to populate the value.
    print(sandbox.name)

    # This doesn't require an additional request, because the request
    # for .name also populated it, but this only applies for certain
    # sets of properties.
    print(sandbox.description)
```

```python
with chatexchange.Client(host, email, password) as chat:
    # Ihis ID isn't valid...
    nonexistent_room = chat.get_room(99999999)

    # ...but we don't send a request with it until here, so this is
    # where the exception will be thrown.
    print(nonexistent_room.name)
```

**For each `Client`, only one instance of each of these classes will be created with a given `.id`.** If you call `client.get_room(1)`, and an instance of `Room` with `.id == 1` for that `Client` already exists (and hasn't been garbage-collected), you'll get a reference to the existing instance. You won't have to re-request data that we already have in memory.

```python
with chatexchange.Client(host, email, password) as chat:
    my_user = chat.get_me()

    # The same instance is returned from get_user(id) as we got from get_me().
    assert my_user is chat.get_user(my_user.id)
```

Also, you should note that **most action methods currently return `None` immediately and don't provide any direct way to know whether they were successful**. If you need to be sure that an action took place, you probably need to verify it separately.

## `Room` objects

A chat room on the chat network, such as from `Client`'s `.get_room(id)`.


```python
from chatexchange import events

with chatexchange.Client(host, email, password) as chat:
    sandbox = chat.get_room(1)
    sandbox.join()

    print("Joined room %s (%s)" % (sandbox.name, sandbox.description))

    print("Users currently in room: %s" % (", ".join(
        user.name for user in sandbox.get_current_users())))

    for event in sandbox.new_events():
        if isinstance(event, events.UserEntered):
            print("A user entered: %s" % (event.user.name))
        elif isinstance(event, events.UserLeft):
            print("A user left: %s" % (event.user.name))
```

### Properties

- `.id:int`
- `.name:str` The current name of that chat room (plain text).
- `.description:str` The current description of the chat room (html source).
- `.message_count:int` The total number of messages that have been sent in this chat room.
- `.user_count:int` The total number of users who have ever participated in this chat room.
- `.parent_site_name:str|None` The name of the parent site this chat room is associated with (plain text), or `None` if it isn't assocaited with any.
- `.owners:User[]` A list of the owners of this chat room as `User`s.
- `.tags:str[]` A list of tags assocaited with this chat room (plain text).

### Methods

- `.join()` Joins the chat room, allowing you to send messages and watch live activity.
- `.leave()` Leaves that chat room.
- `.send_message(str)` Sends a message to this chat room.
- `.watch(callback)` Registers a callback that will be called as `callback(event, client)` for every `Event` in this chat room.
- `.new_messages():Message[]` Produces an infinite generator that will yield every new `Message` sent in this chat room.
- `.new_events(Class?):Event[]` Produces an infinite generator that will yield every new `Event` seen (optionally filtered by event type) in this chat room.
- `.current_users():User[]` Gets a list of users who are currently in the chat room.
- `.pingable_users():User[]` Gets a list of users who are currently "pingable" (will recieve notifications if they're mentioned) in the chat room.

## `Event` objects

There are dozens of types of events that we can observe in a `Room` using its `.new_events(Class?):Event[]` method, including `UserEntered`, `MessageMovedIn`, and `RoomNameChanged`. The `chatexchange.events` module includes a `chatexchange.events.Event` subclass for each of them.

Each `Event` instance holds raw event data we got from the server. Some subclasses provide richers interfaces for that data, but not all of them. The details of the different event subclasses aren't documented here.

### Common Properties

- `.data:dict` The raw event data we got from the server.
- `.room:Room|None` The room the event is associated with, or None.
- `.time_stamp:int`

## `Message` objects

A message on the chat network, such as from `Client`'s `.get_message(id)`.

```
with chatexchange.Client(host, email, password) as chat:
    me = chat.get_me()

    sandbox = chat.get_room(1)
    sandbox.join()

    sandbox.send_message("I'm going to star the next message I see!")

    for message in sandbox.new_messages():
        if message.owner != me:
            message.reply("You're the lucky one today!")
            message.star()
            break
```

### Properties

- `.id:int`
- `.room:Room` The room the message is in.
- `.content:str` The content of the message (html source).
- `.text_content:str` The text content of the message with any formatting discarded (plain text).
- `.content_source:str` The original un-rendered markdown content of the message (markdown source).
- `.owner:User` The User who sent the message.
- `.stars:int` The number of stars the message has.
- `.starred_by_you:bool` Whether the authenticated user starred the message.
- `.pinned:bool` Whether the message is pinned.

### Methods

- `.reply(str)` Sends a message replying to the message.
- `.edit(str)` Edits the message.
- `.delete()` Deletes the message.
- `.star(bool?)` Stars the message (or unstars if you specify `False`)
- `.pin(bool?)` Pins the message (or unstars if you specify `False`)
- `.cancel_stars()` Clears all stars on the message.

## `User` objects

A user account on the chat network, such as from `Client`'s `.get_user(id)` or `.get_me()`.

```python
with chatexchange.Client(host, email, password) as chat:
    community_bot = chat.get_user(-1)

    assert community_bot.name == "Community"

    me = chat.get_me()

    if me.is_moderator:
        print("Activating Self-Destruct Sequence")
    else:
        print("Access Denied")
```

Note that the chat user ID may not correspond with an ID on any other site. It will for most `chat.stackoverflow.com` and `chat.meta.stackexchange.com` users, but not for `chat.stackexchange.com` users, or bots, or some users whose accounts have been merged or deleted.

### Properties

- `.id:int`
- `.name:str` The user's display name (plain text).
- `.about:str` The user's "about me" bio on chat (plain text).
- `.is_moderator:bool` Whether the chat account is flagged as a moderator.
- `.message_count:int` The number of chat messages the user has sent.
- `.room_count:int` The number of chat rooms the user has participated in.
- `.reputation:int` The total reputation of associated accounts.
- `.last_seen:int` Approximate number of seconds since the user was last seen.



 [ChatExchange]: https://github.com/Manishearth/ChatExchange/
 [chat.se]: https://chat.stackexchange.com/
 [epydocs]: https://banks.gitlab.io/ChatExchange/epydocs/
 [Stack Exchange OpenID]: https://openid.stackexchange.com/