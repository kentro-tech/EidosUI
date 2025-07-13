"""EidosUI Markdown Plugin - Theme-aware markdown rendering

This plugin provides markdown rendering that automatically integrates with
EidosUI themes through CSS variables.

Basic usage:
    from eidos.plugins.markdown import Markdown, MarkdownCSS

    # In your document head
    MarkdownCSS()

    # In your content
    Markdown("# Hello World\\n\\nThis is **markdown**!")
"""

from .components import Markdown, MarkdownCSS
from .renderer import MarkdownRenderer

__all__ = ["Markdown", "MarkdownCSS", "MarkdownRenderer"]

__version__ = "0.1.0"
