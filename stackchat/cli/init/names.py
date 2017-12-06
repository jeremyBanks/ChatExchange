import random


# roughly normalize lengths
_CONSONANTS = 'BCDFGHJKLMNPQRSTVXZWY' * 1
_VOWELS =     'AEIOU' * 4
_DIGITS =     '0123456789' * 2
_BREAK  =     ' ' * 20

_pairs = {}
_pairs[' '] = (
    20 * _CONSONANTS.upper() +
    12 * _VOWELS.upper() +
    4 * _VOWELS.lower() +
    2 * _CONSONANTS.lower() +
    1 * _DIGITS
)
for c in _CONSONANTS.upper():
    _pairs[c] = (
        20 * _VOWELS.lower() +
        3 * _CONSONANTS.upper() +
        2 * _CONSONANTS.lower() +
        1 * _VOWELS.upper() +
        1 * _DIGITS +
        1 * _BREAK
    )
for c in _CONSONANTS.lower():
    _pairs[c] = (
        30 * _VOWELS.lower() +
        2 * _VOWELS.upper() +
        1 * _CONSONANTS.upper() +
        1 * _CONSONANTS.lower() +
        1 * _DIGITS +
        22 * _BREAK
    )
for c in _VOWELS.upper() + _VOWELS.lower():
    _pairs[c] = (
        30 * _CONSONANTS.lower() +
        3 * _VOWELS.lower() +
        2 * _CONSONANTS.upper() +
        1 * _VOWELS.upper() +
        22 * _BREAK +
        1 * _DIGITS
    )
for c in _DIGITS:
    _pairs[c] = (
        5 * _DIGITS +
        1 * _CONSONANTS.upper() +
        1 * _VOWELS.upper() +
        1 * _CONSONANTS.lower() +
        1 * _VOWELS.lower() +
        2 * _BREAK
    )

_all_characters = set()
for key, value in _pairs.items():
    _all_characters.update(key, value)
for c in _all_characters:
    if c in ' ': continue # it's a special case

    # add a chance of anything linking to anything else
    _pairs[c] += _pairs.setdefault(c, '') + ''.join(_all_characters)

# The "Tim factor"
_pairs[' '] += len(_pairs[' ']) // 2 * 'T'
_pairs['T'] += len(_pairs['T']) // 1 * 'i'
_pairs['t'] += len(_pairs['t']) // 3 * 'i'
_pairs['i'] += len(_pairs['i']) // 3 * 'm'
_pairs['m'] += len(_pairs['m']) // 2 * ' '

def generate(min_lenght=4, max_length=16):
    current = ''
    last_c = ' '
    while True:
        distribution = _pairs[last_c]
        next_c = random.choice(distribution)

        if next_c == ' ' and last_c == ' ':
            continue # nope
        if next_c == ' ' and random.random() < 2 / len(current):
            continue # don't start with just a letter
        if next_c != ' ' and random.random() > 6 / (len(current) + 1):
            next_c = ' '

        current = current + next_c
        length = len(current.strip())

        if length >= max_length:
            break
        elif next_c == ' ' and length >= min_lenght:
            if random.random() > .25:
                break

        last_c = next_c

    return current.strip()
