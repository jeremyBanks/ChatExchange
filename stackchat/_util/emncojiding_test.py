from .emncojiding import encode, decode


def test():
    originals = [
        b'',
        b'hello world',
        b'\u1234\u0000',
        b'goodbye!',
    ]

    for original in originals:
        encoded = encode(original)
        decoded = decode(encoded)
        assert decoded == original

        reencoded = encode(decoded)
        redecoded = decode(reencoded)
        assert redecoded == original

        if original:
            # encoding isn't a no-op
            assert original != encoded
            assert original != reencoded

            # encoding is different each time
            assert encoded != reencoded
