"""Helper functions for easy EidosUI integration"""

import importlib.resources
from pathlib import Path
from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import fastapi_tags as ft


def get_theme_css(theme: str = "light") -> str:
    """Get CSS content for a theme directly from the package"""
    with importlib.resources.open_text("eidos.themes", f"{theme}.css") as f:
            return f.read()

def get_eidos_js() -> str:
    """Get JavaScript content directly from the package"""
    with importlib.resources.open_text("eidos.static", "eidos-ui.js") as f:
        return f.read()

def serve_eidos_static(app: FastAPI, prefix: str = "/eidos") -> None:
    """
    Mount EidosUI static files to a FastAPI app
    
    Args:
        app: FastAPI application instance
        themes: List of theme names to mount (default: ["light", "dark"])
        prefix: URL prefix for static files (default: "/eidos")
    """
    with importlib.resources.path("eidos", "static") as static_path:
        app.mount(f"{prefix}/static", StaticFiles(directory=str(static_path)), name="eidos_static")
    
    with importlib.resources.path("eidos", "themes") as themes_path:
        app.mount(f"{prefix}/themes", StaticFiles(directory=str(themes_path)), name="eidos_themes")


def create_eidos_head_components(
    themes: list = ['light', 'dark'],
    prefix: str = "/eidos",
    auto_theme: bool = True
):
    """Create EidosUI head components (CSS + JS only)"""
    
    head_content = []

    # Add EidosUI component styles
    head_content.append(ft.Link(rel="stylesheet", href=f"{prefix}/static/eidos-styles.css"))
    
    # Configure themes
    if themes:
        theme_dict = {theme: f"{prefix}/themes/{theme}.css" for theme in themes}
        head_content.append(ft.Script(f"window.EIDOS_THEMES = {theme_dict};"))
    
    if not auto_theme:
        head_content.append(ft.Script("window.EIDOS_NO_AUTO_THEME = true;"))
    
    # Add JS script last
    head_content.append(ft.Script(src=f"{prefix}/static/eidos-ui.js"))
    
    return head_content


