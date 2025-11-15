"""EidosUI Components Package

Higher-level components built on top of the base tags.
"""

from .chat import Chat, ChatContainer, ChatInput, ChatMessage
from .headers import EidosHeaders
from .navigation import NavBar
from .table import DataTable
from .tabs import AlpineTabs, HTMXTabs
from .theme import ThemeSwitch

__all__ = [
    "Chat",
    "ChatContainer",
    "ChatInput",
    "ChatMessage",
    "DataTable",
    "NavBar",
    "EidosHeaders",
    "AlpineTabs",
    "HTMXTabs",
    "ThemeSwitch",
]
