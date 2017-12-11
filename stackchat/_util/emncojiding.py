import base64
import hashlib
import hmac
import zlib

import cryptography.fernet


class Emncojider(object):
    _digits = (
        '0123456789abcdef!?~=-%#ʘ/ΣĐ&Λ*Ψµᢵᣦᣌ'
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
        '÷þ¿±¢$£¥×¡Δχ€‘’Ξᴥᴪᴣ'
    )
    assert 0x100 == len(_digits) == len(set(_digits))

    def __init__(self, key=None):
        if key == None:
            self._key = b'\x00' * 32
        else:
            self._key = bytes(key)

        self._fernet = cryptography.fernet.Fernet(base64.urlsafe_b64encode(self._key))
        self._nonrandom_header_length = 9

    def encode(self, bs):
        compressed = zlib.compress(bs, level=9)
        safe_bytes = self._fernet.encrypt(compressed)
        fer_bytes = bytearray(base64.urlsafe_b64decode(safe_bytes))
        mask = hmac.new(self._key, fer_bytes[self._nonrandom_header_length:], hashlib.sha256).digest()
        for i in range(self._nonrandom_header_length):
            fer_bytes[i] ^= mask[i]
        return ''.join(self._digits[b] for b in fer_bytes)

    def decode(self, s):
        fer_bytes = bytearray(self._digits.index(c) for c in s)
        mask = hmac.new(self._key, fer_bytes[self._nonrandom_header_length:], hashlib.sha256).digest()
        for i in range(self._nonrandom_header_length):
            fer_bytes[i] ^= mask[i]
        safe_bytes = base64.urlsafe_b64encode(fer_bytes)
        compressed = self._fernet.decrypt(safe_bytes)
        return zlib.decompress(compressed)


encode = Emncojider().encode
decode = Emncojider().decode
