import datetime
import setuptools



with open('stackchat/version.py') as f:
    # hack to avoid importing and initializing the rest of the package before setup.
    version = (lambda g={}: [exec(f.read(), {}, g), g][-1])()['__version__']

if version.endswith('.dev'):
    version += str(int(datetime.datetime.utcnow().timestamp()))


setuptools.setup(
    name='stack.chat',
    version=version,
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
