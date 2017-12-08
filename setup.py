import datetime
import os.path
import re
import setuptools



def _read(name):
    with open(os.path.join(os.path.dirname(__file__), name), 'rt', encoding='utf-8') as f:
        return f.read()


def setup():
    name = 'stack.chat'

    version = (lambda g={}: (exec(_read('./stackchat/_version.py'), {}, g), g)[-1])()['__version__']
    if version.endswith('.dev'):
        version += str(int(datetime.datetime.utcnow().timestamp()))

    readme = _read('./README.md')

    one_sentence = readme
    one_sentence = re.split(r'(?:%s|this)\s+is\s+' % (re.escape(name)), one_sentence, 1, re.IGNORECASE)[1]
    one_sentence = re.split(r'(?:[\.\!][\s$]|\n\n)', one_sentence, 1)[0]
    one_sentence = re.sub(r'\s+', ' ', one_sentence).strip()

    return setuptools.setup(
        name=name,
        version=version,
        description=one_sentence,
        long_description=None, # wait until the readme is less awful
        python_requires='>=3',
        install_requires=[
            'SQLAlchemy',
            'lxml',
            'html5lib',
            'hashids',
            'pprintpp',
            'aiohttp',
            'aiodns',
            'cssselect',
            'aitertools',
            'toml',
            'docopt',
        ],
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
            'License :: OSI Approved :: MIT License',
        ],
        url='https://stack.chat',
        author='Jeremy Banks',
        author_email='_@jeremy.ca',
        license='MIT',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'stack.chat=stackchat.__main__:main',
                'stackchat=stackchat.__main__:main',
            ],
        },
    )


if __name__ == '__main__':
    setup()

