"""EidosUI Components Package

Higher-level components built on top of the base tags.
"""

from .feedback import Feedback
from .headers import EidosHeaders
from .navigation import NavBar
from .table import DataTable
from .tabs import AlpineTabs, HTMXTabs
from .theme import ThemeSwitch

__all__ = [
    "DataTable",
    "NavBar",
    "EidosHeaders",
    "AlpineTabs",
    "HTMXTabs",
    "ThemeSwitch",
    "Feedback",
]
