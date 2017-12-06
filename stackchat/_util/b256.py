import base64
import hashlib

import cryptography.fernet



_digits = (
    '0123456789abcdef!?~=-hijlΣĐrΛtΨwxyz'
    '😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏'
    '😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟'
    '😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯'
    '😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿'
    '🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏'
    '🤐🤑🤒🤓🤔🤕🤖🤗🤘🤙🤚🤛🤜🤝🤞🤠'
    '🤡🤢🤣🤤🤥🤦🤧🤳🤴🤵🤶🤷🤸🤹🤺'
    '🤼🤽🤾🥀🥁🥂🥃🥄🥅🥇🥈🥉🥊🥋🥐'
    '🥑🥒🥔🥕🥖🥗🥘🥙🥚🥛🥜🥝🥞🦀🦁'
    '🏃🏄🏇🏊🏋👃👆💆💇💪🕴🕵🕺🖐🏂'
    '🦂🦃🦄🦅🦆🦇🦈🦉🦊🦋🦌🦍🦎🦏🦐🦑'
    '👇👈👉👊👋👌👍👎👏👐👦👧👨👩👮👰'
    '👱👲👳👴👵👶👷👸👼💁💂💃💅⛽'
    '÷þ¿±¢$£¥×¡Δχ€‘’ΞXYZ'
)
assert 0x100 == len(_digits) == len(set(_digits))


_key = b'\x00' * 32
_obfuscator = cryptography.fernet.Fernet(base64.urlsafe_b64encode(_key))
_nonrandom_header_length = 9


def encode(bs):
    safe_bytes = _obfuscator.encrypt(bs)
    fer_bytes = bytearray(base64.urlsafe_b64decode(safe_bytes))
    iv = fer_bytes[_nonrandom_header_length:]
    mask = hashlib.sha256(iv).digest()
    for i in range(_nonrandom_header_length):
        fer_bytes[i] ^= mask[i]
    return ''.join(_digits[b] for b in fer_bytes)


def decode(s):
    fer_bytes = bytearray(_digits.index(c) for c in s)
    iv = fer_bytes[_nonrandom_header_length:]
    mask = hashlib.sha256(iv).digest()
    for i in range(_nonrandom_header_length):
        fer_bytes[i] ^= mask[i]
    safe_bytes = base64.urlsafe_b64encode(fer_bytes)
    return _obfuscator.decrypt(safe_bytes)
