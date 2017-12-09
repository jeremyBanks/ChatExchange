"""
usage:
    stack.chat config get KEY
    stack.chat config set KEY VALUE
    stack.chat config delete KEY
    stack.chat config --help
    stack.chat --help

Reads from local if specified there, else reads global, else reads default.

Writes to local if exists, else writes to global.

command options:
    --local
    --global
"""


async def main(chat, opts):
    raise NotImplementedError()
