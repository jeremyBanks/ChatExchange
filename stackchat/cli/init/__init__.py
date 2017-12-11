"""
usage:
    stack.chat init [--global] [--email=EMAIL] [--password=PASSWORD]
    stack.chat init --help
    stack.chat --help

Interactively initializes the stack.chat config and data store, either
locally (in the current directory) or globally (in the home directory).
"""


import asyncio
import logging
import random

import docopt



logger = logging.getLogger(__name__)


NO_CHAT = True


SE_HOSTS = [
    'math', 'softwareengineering', 'unix', 'english', 'apple', 'android',
    'stats', 'codereview', 'security', 'physics', 'tex', 'electronics',
    'gaming', 'dba', 'wordpress', 'gamedev', 'ux', 'gis', 'graphicdesign',
    'scifi', 'cs', 'networkengineering', 'puzzling', 'arduino', 'music',
    'skeptics', 'softwarerecs', 'rpg', 'biology', 'bicycles'
]
random.shuffle(SE_HOSTS)
SE_HOSTS = SE_HOSTS[:random.randint(21, len(SE_HOSTS))]


async def main(config, opts):
    location = '--local' if not opts['--global'] else '--global'

    se_email = config['se_email']
    se_password = config['se_password']
    db_path = config['db_path']
