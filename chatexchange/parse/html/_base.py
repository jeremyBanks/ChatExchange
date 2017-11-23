import logging
import re
import warnings
from html import escape as escape_html

import lxml.html
import lxml.html.html5parser
import lxml.etree

from .._base import Parse



logger = logging.getLogger(__name__)


def _monkeypatch_html5lib():
    html = '''&#1;&#0;<b &#1;&#0;>&#1;&#0;</b>&#1;&#0;'''
    # there is no acceptable way to hook into attribute values to ensure they're legal, as in:
    # html = '''&#1;&#0;<b &#1;&#0; id="&#1;&#0;">&#1;&#0;</b>&#1;&#0;'''

    try:
        lxml.html.html5parser.HTMLParser().parse(html)
        logger.debug("Monkeypatching skipped because lxml.html.HTMLParser() was already behaving correctly.")
        return
    except ValueError:
        pass

    # lxml only allows characters that are valid in XML, but the web is dark and full of terrors.
    # it looks like html5lib tries to handle this with InfosetFilter, but coerceCharacters
    # doesn't filter out the right things. Maybe see about fixing upstream if confident.
    # see https://stackoverflow.com/a/25920392/1114
    import html5lib._ihatexml

    xml_illegal_re = re.compile('[^\u0020-\uD7FF\u0009\u000A\u000D\uE000-\uFFFD\U00010000-\U0010FFFF]')
    def strip_illegal(s):
        sp = xml_illegal_re.sub('�', s)
        if sp != s:
            warnings.warn("non-XML-legal character(s) mangled", html5lib._ihatexml.DataLossWarning)
        return sp

    for name in ['coerceCharacters', 'toXmlName']:
        old = getattr(html5lib._ihatexml.InfosetFilter, name)
        new = lambda self, s: strip_illegal(s)
        setattr(html5lib._ihatexml.InfosetFilter, name, new)

    try:
        lxml.html.html5parser.HTMLParser().parse(html)
        logger.debug("Monkeypatching successfully fixed lxml.html.HTMLParser().")
    except ValueError:
        logger.error("Monkeypatching unexpectedly failed to fix lxml.html.HTMLParser.")


with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    _monkeypatch_html5lib()


class ParseHTML(Parse):
    # Namespaced HTML elements seem to be incompatible with .cssselect().
    _parser = lxml.html.html5parser.HTMLParser(namespaceHTMLElements=False)

    def __init__(self, data):
        if isinstance(data, lxml.etree.ElementBase):
            self._dom = data
        else:
            assert isinstance(data, str)
            logger.debug("Parsing HTML to DOM...")
            self._dom = self._parser.parse(data).getroot()

    @staticmethod
    def _dom_outer_html(dom):
        return lxml.html.tostring(dom, encoding=str, with_tail=False)

    @staticmethod
    def _dom_inner_html(dom):
        return escape_html(dom.text, False) + ''.join(
            lxml.html.tostring(child_dom, encoding=str, with_tail=True)
            for child_dom in dom.iterchildren())

    @staticmethod
    def _dom_text_content(dom):
        return lxml.html.tostring(dom, encoding=str, method='text')
