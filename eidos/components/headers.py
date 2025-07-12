from air import Meta, Script, Link, Html, Head, Title
from ..tags import Body

def get_css_urls():
    """Return list of CSS URLs for EidosUI."""
    return [
        "/eidos/css/styles.css",
        "/eidos/css/themes/eidos-variables.css", 
        "/eidos/css/themes/light.css",
        "/eidos/css/themes/dark.css"
    ]

def EidosHeaders(include_tailwind=True, include_lucide=False, theme="light"):
    """Standard EidosUI headers with CSS includes.
    
    Args:
        include_tailwind: Whether to include Tailwind CSS CDN
        include_lucide: Whether to include Lucide Icons CDN (Activate with `Script("lucide.createIcons();")` in your page)
        theme: Theme to use (light or dark)
    """
    headers = [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    ]
    
    if include_tailwind:
        headers.append(Script(src="https://cdn.tailwindcss.com"))

    if include_lucide:
        headers.append(Script(src="https://unpkg.com/lucide@latest"))
    
    # Add EidosUI CSS files
    for css_url in get_css_urls():
        headers.append(Link(rel="stylesheet", href=css_url))
    
    # Set initial theme
    headers.append(Script(f"document.documentElement.setAttribute('data-theme', '{theme}');"))
    
    return headers