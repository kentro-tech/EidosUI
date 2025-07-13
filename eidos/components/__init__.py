"""EidosUI Components Package

Higher-level components built on top of the base tags.
"""

from .headers import EidosHeaders
from .navigation import NavBar
from .table import DataTable

__all__ = ["DataTable", "NavBar", "EidosHeaders"]
