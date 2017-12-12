"""
usage:
    stack.chat config get [--default|--global] [KEY_PATH]
    stack.chat config set --global KEY_PATH STRING_VALUE
    stack.chat config delete --global KEY_PATH
    stack.chat config --help
    stack.chat --help
"""


import toml


def _update_dict(target, source):
    pass


class Config(object):
    def __init__(self, *datas):
        self.data = {}
        for data in datas:
            if isinstance(data, dict):
                _update_dict(self.data, data)
            else:
                _update_dict(self.data, data.data)

    def update(self, data):
        pass



def read():
    default_config = Config({
        'credentials': {
            'stack-exchange': {
                'email': '',
                'password': '',
            },
        },
        'resources': {
            'db': 'sqlite:///:memory:',
        },
        'state': {
            'room-last-tailed': {
                '0': 0,
            },
        },
    })
    global_config = Config(toml.loads(open('~/.stack.chat.toml')))
    local_config = Config(
        default_config, global_config, toml.loads(open('./.stack.chat.toml')))
    
    return local_config


def write():
    pass


async def main(chat, opts):
    print(toml.dumps(read()))
    raise NotImplementedError()
