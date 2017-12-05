import datetime
import setuptools


import toml



__version__ = '0.0.1-dev'
if __version__.endswith('-dev'):
    __version__ += str(int(datetime.datetime.utcnow().timestamp()))


with open('Pipfile', 'rt') as f:
    install_requires = list(toml.load(f)['packages'].keys())


setup = lambda: setuptools.setup(
    name='stack.chat',
    version=__version__,
    python_requires='>=3',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: MIT License',
    ],
    url='https://stack.chat',
    author='Jeremy Banks',
    author_email='_@jeremy.ca',
    license='MIT',
    packages=['stackchat'],
    entry_points={
        'console_scripts': [
            'stack.chat=stackchat.__main__:main',
            'stackchat=stackchat.__main__:main',
        ]
    })


if __name__ == '__main__':
    setup()
