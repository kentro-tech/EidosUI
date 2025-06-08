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


def get_eidos_css_links(themes: list = ["light", "dark"], prefix: str = "/eidos") -> str:
    """Generate CSS link tags for themes"""
    links = []
    for theme in themes:
        links.append(f'<link rel="stylesheet" href="{prefix}/themes/{theme}.css">')
    return "\n".join(links)


def get_eidos_js_script(prefix: str = "/eidos") -> str:
    """Generate script tag for EidosUI JavaScript"""
    return f'<script src="{prefix}/static/eidos-ui.js"></script>'


def create_eidos_head(
    title: str = "EidosUI App",
    themes: list = ["light", "dark"],
    prefix: str = "/eidos",
    include_tailwind: bool = True
) -> str:
    """Create HTML head content (just the inner content, not the <head> tags)"""
    head_parts = [
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<title>{title}</title>'
    ]
    
    if include_tailwind:
        head_parts.append('<script src="https://cdn.tailwindcss.com"></script>')
    
    head_parts.append(get_eidos_css_links(themes, prefix))
    head_parts.append(get_eidos_js_script(prefix))
    
    return "\n".join(head_parts)


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


def inline_eidos_css(themes: list = ["light", "dark"]) -> str:
    """Get all CSS as inline styles (for single-file deployments)"""
    css_content = []
    for theme in themes:
        content = get_theme_css(theme)
        if content:
            css_content.append(content)
    
    if css_content:
        return f"<style>\n{chr(10).join(css_content)}\n</style>"
    return ""


def inline_eidos_js() -> str:
    """Get JavaScript as inline script (for single-file deployments)"""
    js_content = get_eidos_js()
    if js_content:
        return f"<script>\n{js_content}\n</script>"
    return ""


def create_inline_eidos_head(
    title: str = "EidosUI App",
    themes: list = ["light", "dark"],
    include_tailwind: bool = True
) -> str:
    """Create HTML head content with inline EidosUI assets (no external files needed)"""
    head_parts = [
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<title>{title}</title>'
    ]
    
    if include_tailwind:
        head_parts.append('<script src="https://cdn.tailwindcss.com"></script>')
    
    # Inline CSS and JS
    head_parts.append(inline_eidos_css(themes))
    head_parts.append(inline_eidos_js())
    
    return "\n".join(head_parts) 


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


def create_inline_eidos_head_tag(
    title: str = "EidosUI App",
    themes: list = ["light", "dark"],
    include_tailwind: bool = True
):
    """Create a fastapi-tags Head component with inline EidosUI assets"""
    import fastapi_tags as ft
    
    head_content = []
    
    head_content.extend([
        ft.Meta(charset="UTF-8"),
        ft.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        ft.Title(title)
    ])
    
    if include_tailwind:
        head_content.append(ft.Script(src="https://cdn.tailwindcss.com"))
    
    # Add inline CSS
    css_content = inline_eidos_css(themes)
    if css_content:
        head_content.append(ft.Style(css_content))
    
    # Add inline JS
    js_content = get_eidos_js()
    if js_content:
        head_content.append(ft.Script(js_content))
    
    return ft.Head(*head_content)