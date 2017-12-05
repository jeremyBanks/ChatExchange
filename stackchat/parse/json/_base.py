import datetime
import json
import logging
import re
import warnings

from .._base import Parse



logger = logging.getLogger(__name__)


class ParseJSON(Parse):
    _parser = json.JSONDecoder()

    def __init__(self, data):
        if isinstance(data, dict):
            self._data = data
        else:
            assert isinstance(data, str)
            logger.debug("Parsing JSON...")
            self._data = self._parser.decode(data)
