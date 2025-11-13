"""Markdown components for EidosUI"""

import air

from .renderer import MarkdownRenderer

# Global renderer instance for reuse
_renderer = MarkdownRenderer()


def Markdown(content: str, class_: str | None = None, **kwargs) -> air.Div:
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

    return air.Div(air.Raw(html_content), class_=class_, **kwargs)


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
        type="text/css",
    )
