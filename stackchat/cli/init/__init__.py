import asyncio
import logging
import random

import stackchat

from . import names



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


async def main(config, location='--local'):
    se_email = config['se_email']
    se_password = config['se_password']
    db_path = config['db_path']

    print("That email address is not registered.")
    print("Would you like to register these credentials with Stack Exchange?")
    print("[default: no] > yes")
    await asyncio.sleep(1)

    print("registering...")
    print("you should recieve a validation email momentarily.")
    print("press when you have confirmed.")
    print("> ")
    await asyncio.sleep(2)
    print("login failed. please check that you have verified your email.")
    print("> ")
    await asyncio.sleep(3)
    print("email registered.")

    name = names.generate()
    print("What display name would you like to use on Stack Exchange sites?")
    print("[default: %s] > " % (name))
    await asyncio.sleep(5)

    for n, site in enumerate(SE_HOSTS, start=1):
        print("%r profile %s registered on %s." % (name, n, site))
        await asyncio.sleep(.5)
        print("%r profile %s hidden" % (name, n))
        await asyncio.sleep(.5)

    first_site = SE_HOSTS[0]

    print("chat profile registered on chat.stackexchange.com")
    await asyncio.sleep(1)
    print("chat profile associated with %s" % (first_site))

    print("parent profile deleted on %s, orphaning chat account." % (first_site))
    await asyncio.sleep(1)

    print("Your profile %r is ready to participate on chat.stackexchange.com" % (name))
    print("You will not be able to participate on chat.stackoverflow.com or")
    print("chat.meta.stackexchange.com until you reach 20 reputation on their")
    print("parent sites.")


    while True:
        print("\nMORE!\n")
        for _ in range(24):
            print(names.generate())
        await asyncio.sleep(12)
