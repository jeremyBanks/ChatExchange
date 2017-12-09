"""
usage:
    stack.chat [-q|-v] COMMAND [ARGS...]
    stack.chat COMMAND --help
    stack.chat --help
    stack.chat --version

general options:
    --quiet, -q    Minimal logging output.
    --verbose, -v  Maximum logging output.

common commands:
    init    Initialize config and data store with credentials.
    tail    Display the latest message in a chat room.
    send    Send a message to a chat room.
    web     Launch local dev web UI.
"""


import asyncio
import getpass
import importlib
import logging
import os

import docopt
import toml

from .._version import __version__
from ..client import Client



logger = logging.getLogger(__name__)


def main(*argv):
    opts = docopt.docopt(
        __doc__.replace('stack.chat', argv[0]),
        argv[1:],
        True,
        "stack.chat version %s" % (__version__),
        True)

    # docopt() will exit when it handles --version and --help for us.
    # we also alias them as these psuedo-commands.
    if opts['COMMAND'] == 'version':
        return main(argv[0], '--version')
    if opts['COMMAND'] == 'help':
        command_arg = opts['ARGS'][:1]
        return main(argv[0], *command_arg, '--help')

    if opts['--quiet']:
        level = logging.ERROR
    elif opts['--verbose']:
        level = logging.DEBUG
    else:
        level = logging.WARNING

    logging.basicConfig(format="%(e)32s %(relative)6s ms%(n)s%(levelled_name)32s %(message)s", level=level)
    for handler in logging.getLogger().handlers:
        handler.addFilter(Filter())

    logger.debug("optparse opts: %s" % opts)

    subcommand = opts['COMMAND']

    subcommand_module = importlib.import_module('.' + subcommand, 'stackchat.cli')
    no_chat = getattr(subcommand_module, 'NO_CHAT', False)

    logger.debug('subcommand_module == %r', subcommand_module)

    se_email, se_password = None, None
    
    try:
        with open(os.path.expanduser('~/.stack.chat.toml')) as f:
            global_conf = toml.load(f)
            logger.debug("read global config: %r", global_conf)
    except IOError:
        global_conf = {'credentials': {'stack-exchange': {}}}
    
    try:
        with open('./.stack.chat.toml') as f:
            local_conf = toml.load(f)
            logger.debug("read local config: %r", local_conf)
    except IOError:
        local_conf = {'credentials': {'stack-exchange': {}}}

    if not se_email:
        se_email = os.environ.get('STACK_EXCHANGE_EMAIL')
    if not se_email:
        se_email = local_conf['credentials']['stack-exchange'].get('email')
    if not se_email:
        se_email = global_conf['credentials']['stack-exchange'].get('email')
    if not se_email:
        se_email = os.environ.get('ChatExchangeU')
    if not se_email:
        se_email = input("stack exchange login email: ")

    if not se_password:
        se_password = os.environ.get('STACK_EXCHANGE_PASSWORD')
    if not se_password:
        se_password = local_conf['credentials']['stack-exchange'].get('password')
    if not se_password:
        se_password = global_conf['credentials']['stack-exchange'].get('password')
    if not se_password:
        se_password = os.environ.get('ChatExchangeP')
    if not se_password:
        se_password = getpass.getpass("stack exchange password: ")

    db_path = 'sqlite:///./.stack.chat.sqlite'

    # re-construct without flags we handle above
    sub_argv = [argv[0], subcommand, *opts['ARGS']]

    if getattr(subcommand_module, '__doc__', None):
        sub_opts = docopt.docopt(
            subcommand_module.__doc__.replace('stack.chat', argv[0]),
            argv[1:],
            True,
            False)
        logger.debug("subcommand optparse opts: %s" % opts)
    else:
        sub_opts = None

    if not no_chat:
        with Client(db_path, se_email, se_password) as chat:
            coro = subcommand_module.main(chat, sub_opts)
            asyncio.get_event_loop().run_until_complete(coro)
    else:
        coro = subcommand_module.main(dict(locals()), sub_opts)
        asyncio.get_event_loop().run_until_complete(coro)


class Filter(logging.Filter):
    last = 0

    def filter(self, record):
        # see https://stackoverflow.com/a/43052949/1114
        delta = record.relativeCreated - self.last
        record.relative = '+{0:.0f}'.format(delta)
        record.e = ''
        record.n = '\n'
        record.levelled_name = '%s/%-5s' % (record.name, record.levelname)

        self.last = record.relativeCreated
        return True
