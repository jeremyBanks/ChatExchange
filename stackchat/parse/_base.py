import datetime

from .._util import obj_dict



class Parse:
    __repr__ = obj_dict.repr

    @staticmethod
    def _parse_age_ago(text):
        suffixes = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
            'y': 31536000
        }
        if text == "n/a":
            return -1  # Take this as an error code if you want
        if text == "just now":
            return 0
        splat = text.split(' ')
        assert len(splat) == 2, "text doesn't appear to be in <x ago> format"
        char = splat[0][-1]
        number = int(splat[0][:-1])
        assert char in suffixes, "suffix char unrecognized"
        return datetime.timedelta(seconds=number * suffixes[char])
