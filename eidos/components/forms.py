"""Form components for EidosUI"""

import fastapi_tags as ft
from ..core.styles import button_styles, form_styles
from ..core.utils import merge_classes


def Button(*content, cls: str = button_styles.primary, size_cls: str = button_styles.md, **kwargs) -> ft.Button:
    """Highly flexible button component that takes classes directly"""
    return ft.Button(
        *content,
        cls=merge_classes(cls, size_cls),
        **kwargs
    )


def Input(cls: str = form_styles.input, size_cls: str = "", state_cls: str = "", **kwargs) -> ft.Input:
    """Flexible input component with class-based styling"""
    return ft.Input(
        cls=merge_classes(cls, size_cls, state_cls),
        **kwargs
    )


def Textarea(cls: str = form_styles.textarea, **kwargs) -> ft.Textarea:
    """Flexible textarea component"""
    return ft.Textarea(
        cls=cls,
        **kwargs
    )


def Select(*options, cls: str = form_styles.select, **kwargs) -> ft.Select:
    """Flexible select component"""
    return ft.Select(
        *options,
        cls=cls,
        **kwargs
    )


def Label(text: str, cls: str = form_styles.label, **kwargs) -> ft.Label:
    """Flexible label component"""
    return ft.Label(
        text,
        cls=cls,
        **kwargs
    )


def FormGroup(*content, cls: str = form_styles.form_group, **kwargs) -> ft.Div:
    """Form group container with default spacing"""
    return ft.Div(
        *content,
        cls=cls,
        **kwargs
    ) 