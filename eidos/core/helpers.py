"""Helper functions for easy EidosUI integration"""

import importlib.resources
from pathlib import Path
from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def get_theme_css(theme: str = "light") -> str:
    """Get CSS content for a theme directly from the package"""
    try:
        with importlib.resources.open_text("eidos.themes", f"{theme}.css") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def get_eidos_js() -> str:
    """Get JavaScript content directly from the package"""
    try:
        with importlib.resources.open_text("eidos.static", "eidos-ui.js") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def serve_eidos_static(app: FastAPI, prefix: str = "/eidos") -> None:
    """
    Automatically mount EidosUI static files to a FastAPI app
    
    Args:
        app: FastAPI application instance
        prefix: URL prefix for static files (default: "/eidos")
    """
    try:
        # Get the package directory paths
        with importlib.resources.path("eidos", "static") as static_path:
            app.mount(f"{prefix}/static", StaticFiles(directory=str(static_path)), name="eidos_static")
        
        with importlib.resources.path("eidos", "themes") as themes_path:
            app.mount(f"{prefix}/themes", StaticFiles(directory=str(themes_path)), name="eidos_themes")
            
    except Exception as e:
        # Fallback for development - try relative paths
        import os
        package_dir = Path(__file__).parent.parent
        
        if (package_dir / "static").exists():
            app.mount(f"{prefix}/static", StaticFiles(directory=str(package_dir / "static")), name="eidos_static")
        
        if (package_dir / "themes").exists():
            app.mount(f"{prefix}/themes", StaticFiles(directory=str(package_dir / "themes")), name="eidos_themes")


 


def create_eidos_head_tag(
    title: str = "EidosUI App",
    themes: list = ["light", "dark"],
    prefix: str = "/eidos",
    include_tailwind: bool = True
):
    """Create a fastapi-tags Head component with EidosUI setup"""
    import fastapi_tags as ft
    
    head_content = []
    
    head_content.extend([
        ft.Meta(charset="UTF-8"),
        ft.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        ft.Title(title)
    ])
    
    if include_tailwind:
        head_content.append(ft.Script(src="https://cdn.tailwindcss.com"))
    
    # Add CSS links
    for theme in themes:
        head_content.append(ft.Link(rel="stylesheet", href=f"{prefix}/themes/{theme}.css"))
    
    # Add JS script
    head_content.append(ft.Script(src=f"{prefix}/static/eidos-ui.js"))
    
    return ft.Head(*head_content)


