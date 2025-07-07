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
def EidosHeaders(include_tailwind=True, theme="light"):
    """Standard EidosUI headers with CSS includes."""
    headers = [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    ]
    
    if include_tailwind:
        headers.append(Script(src="https://cdn.tailwindcss.com"))
    
    # Add EidosUI CSS files
    for css_url in get_css_urls():
        headers.append(Link(rel="stylesheet", href=css_url))
    
    # Set initial theme
    headers.append(Script(f"document.documentElement.setAttribute('data-theme', '{theme}');"))
    
    return headers