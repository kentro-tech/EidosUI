"""Markdown components for EidosUI"""

import air
from typing import Optional
from .renderer import MarkdownRenderer


# Global renderer instance for reuse
_renderer = MarkdownRenderer()


def Markdown(content: str, class_: Optional[str] = None, **kwargs) -> air.Div:
    """Main markdown component that renders markdown content with theme integration.
    
    Args:
        content: Markdown text to render
        class_: Additional CSS classes to apply
        **kwargs: Additional attributes to pass to the wrapper div
        
    Returns:
        air.Div containing the rendered markdown HTML
    """
    # Render the markdown content
    html_content = _renderer.render(content)
    
    # Create the div with raw HTML content
    if class_:
        return air.Div(
            air.RawHTML(html_content),
            class_=class_,
            **kwargs
        )
    else:
        return air.Div(
            air.RawHTML(html_content),
            **kwargs
        )


def MarkdownCSS() -> air.Link:
    """Returns a link tag to include the markdown CSS.
    
    This should be included in the head of your document to ensure
    markdown styling is available.
    
    Returns:
        air.Link element pointing to the markdown CSS file
    """
    return air.Link(
        rel="stylesheet",
        href="/eidos/plugins/markdown/css/markdown.css",
        type="text/css"
    )