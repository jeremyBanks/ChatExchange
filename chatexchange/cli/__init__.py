import asyncio
import getpass
import importlib
import logging
import os
import sys

import chatexchange



def main():
    command, *args = sys.argv

    logging.getLogger().setLevel(logging.WARNING)
    logging.getLogger('chatexchange').setLevel(logging.DEBUG)

    logging.basicConfig(format="%(e)32s %(relative)6s ms%(n)s%(levelled_name)32s %(message)s", level=logging.DEBUG)
    for handler in logging.getLogger().handlers:
        handler.addFilter(Filter())

    if args:
        subcommand, *subcommand_args = args
        command_module = importlib.import_module('.' + subcommand, 'chatexchange.cli')

        se_email = os.environ.get('STACK_EXCHANGE_EMAIL') or os.environ.get('ChatExchangeU') or ''
        se_password = os.environ.get('STACK_EXCHANGE_PASSWORD') or os.environ.get('ChatExchangeP') or ''

        if not se_email:
            se_email = getpass.getpass("stack exchange login email: ")
            
        if not se_password:
            se_password = getpass.getpass("stack exchange password: ")

        db_path = 'sqlite:///./.ChatExchange.sqlite'

        with chatexchange.Client(db_path, se_email, se_password) as chat:
            coro = command_module.main(chat, *subcommand_args)
            asyncio.get_event_loop().run_until_complete(coro)
    else:
        sys.stderr.write("usage: %s $subcommand [$args...]\n" % (command))
        sys.exit(1)


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
