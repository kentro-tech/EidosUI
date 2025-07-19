"""EidosUI Components Package

Higher-level components built on top of the base tags.
"""

from .headers import EidosHeaders
from .navigation import NavBar
from .table import DataTable
from .tabs import TabContainer, TabList, TabPanel, Tabs

__all__ = [
    "DataTable",
    "NavBar",
    "EidosHeaders",
    "TabContainer",
    "TabList",
    "TabPanel",
    "Tabs",
]
