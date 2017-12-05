"""
Classes interpreting Bonfire's HTML pages and internal JSON responses, sort-of
as reconstructed view models. No HTTP or database logic.
"""

from . import _base
from .json import *
from .html import *
