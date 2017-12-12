stack.chat
==========

stack.chat is an unofficial Python 3 library and command-line tool
for [Stack Exchange chat](https://chat.stackexchange.com/faq).

### Links ###

- [stack.chat](https://stack.chat)
- [github/jeremyBanks/stack.chat](https://github.com/jeremyBanks/stack.chat)
- [pypi/stack.chat](https://pypi.python.org/pypi/stack.chat)
- [stackapps.com/q/7710](https://stackapps.com/q/7710)



Installation
------------

Using your Python 3 package manager of choice:

    pip3 install stack.chat

### For Contributors ###

Contributors who clone this repo can install our dev packages with pipenv:

    pip install pipenv
    pipenv install --dev



Basic Usage
-----------

### CLI ###

The default config uses a temporary in-memory database and requires your
Stack Exchange credentials to be provided through environment variables.
We can see this by checking the current config with `stack.chat config`.

    $ stack.chat config
    # the default config should appear

Instead, we'll want to use `stack.chat init --global` to remember our
credentials and create a persistent local database.

    $ stack.chat init --global
    # TODO: what happens here?
    # seeding database...

    $ stack.chat config
    #

We can confirm it worked with TODO:

    $ stack.chat whoami --server=se

You can read the latest messages in a chat room with `stack.chat tail`.

    $ stack.chat tail --server=se --room=1
    # TODO

Certain common parameters, such as `--server` and `--room`, will be
saved and used as the default if you omit that parameter the next time
it's *required* for a command. TODO

    $ stack.chat tail --since-last --follow
    #
    ^C

Let's TODO!

    $ stack.chat send "hello, world"
    #

More details are available from the application itself.

    $ stack.chat help

### Python ###

The Python interface is not yet stable.

License
-------

Licensed under either of

 - Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE))
 - MIT License ([LICENSE-MIT](LICENSE-MIT))

at your option.

### Contribution ###

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache
License, Version 2.0, shall be dual licensed as above, without any
additional terms or conditions.

### Contributors ###

Please see the Git commit history or
[this list on GitHub](https://github.com/jeremyBanks/stack.chat/contributors).
