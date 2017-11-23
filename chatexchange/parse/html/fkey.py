import datetime
import logging

from ..._util import obj_dict

from ._base import ParseHTML


logger = logging.getLogger(__name__)


class FKey(ParseHTML):
    """
    Any HTML page/fragment that contains an fkey.
    """

    def __init__(self, page):
        super().__init__(page)

        fkey_el ,= self._dom.cssselect('input[name=fkey]')
        self.fkey = fkey_el.get('value')
