"""Semantic typography components for EidosUI"""

import fastapi_tags as ft
from ..core.styles import typography_styles
from ..core.utils import merge_classes


def H1(*content, cls: str = typography_styles.h1, **kwargs) -> ft.H1:
    """Semantic H1 heading"""
    return ft.H1(*content, cls=cls, **kwargs)


def H2(*content, cls: str = typography_styles.h2, **kwargs) -> ft.H2:
    """Semantic H2 heading"""
    return ft.H2(*content, cls=cls, **kwargs)


def H3(*content, cls: str = typography_styles.h3, **kwargs) -> ft.H3:
    """Semantic H3 heading"""
    return ft.H3(*content, cls=cls, **kwargs)


def H4(*content, cls: str = typography_styles.h4, **kwargs) -> ft.H4:
    """Semantic H4 heading"""
    return ft.H4(*content, cls=cls, **kwargs)


def H5(*content, cls: str = typography_styles.h5, **kwargs) -> ft.H5:
    """Semantic H5 heading"""
    return ft.H5(*content, cls=cls, **kwargs)


def H6(*content, cls: str = typography_styles.h6, **kwargs) -> ft.H6:
    """Semantic H6 heading"""
    return ft.H6(*content, cls=cls, **kwargs)


def P(*content, cls: str = typography_styles.body, **kwargs) -> ft.P:
    """Semantic paragraph"""
    return ft.P(*content, cls=cls, **kwargs)


def Text(*content, cls: str = typography_styles.body, **kwargs) -> ft.Span:
    """Generic text span"""
    return ft.Span(*content, cls=cls, **kwargs)


def Em(*content, cls: str = "italic", **kwargs) -> ft.Em:
    """Semantic emphasis (italic)"""
    return ft.Em(*content, cls=cls, **kwargs)


def Strong(*content, cls: str = "font-semibold", **kwargs) -> ft.Strong:
    """Semantic strong emphasis (bold)"""
    return ft.Strong(*content, cls=cls, **kwargs)


def A(*content, href: str = "#", cls: str = "text-[var(--color-primary)] hover:text-[var(--color-primary-hover)] underline underline-offset-2 transition-colors duration-200", **kwargs) -> ft.A:
    """Semantic anchor link"""
    return ft.A(*content, href=href, cls=cls, **kwargs)


def Code(*content, cls: str = typography_styles.code, **kwargs) -> ft.Code:
    """Inline code"""
    return ft.Code(*content, cls=cls, **kwargs)


def Pre(*content, cls: str = "bg-surface border border-border rounded-lg p-4 overflow-x-auto text-sm font-mono", **kwargs) -> ft.Pre:
    """Preformatted text block"""
    return ft.Pre(*content, cls=cls, **kwargs)


# def Blockquote(*content, cls: str = "border-l-4 border-primary pl-6 py-2 italic text-text-muted", **kwargs) -> ft.Blockquote:
#     """Semantic blockquote"""
#     return ft.Blockquote(*content, cls=cls, **kwargs)


def Mark(*content, cls: str = typography_styles.mark, **kwargs) -> ft.Mark:
    """Highlighted text"""
    return ft.Mark(*content, cls=cls, **kwargs)


def Small(*content, cls: str = "text-sm text-text-muted", **kwargs) -> ft.Small:
    """Small text"""
    return ft.Small(*content, cls=cls, **kwargs) 