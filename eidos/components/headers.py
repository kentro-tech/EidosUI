from typing import Literal

from air import Link, Meta, Script, Tag


def get_css_urls() -> list[str]:
    """Return list of CSS URLs for EidosUI."""
    return [
        "/eidos/css/styles.css",
        "/eidos/css/themes/eidos-variables.css",
        "/eidos/css/themes/light.css",
        "/eidos/css/themes/dark.css",
    ]


def EidosHeaders(
    include_tailwind: bool = True,
    include_lucide: bool = True,
    include_eidos_js: bool = True,
    theme: Literal["light", "dark"] = "light",
) -> list[Tag]:
    """Complete EidosUI headers with EidosUI JavaScript support.

    Args:
        include_tailwind: Include Tailwind CSS CDN
        include_lucide: Include Lucide Icons CDN
        include_eidos_js: Include EidosUI JavaScript (navigation, future features)
        theme: Initial theme
    """
    headers = [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    ]

    # Core libraries
    if include_tailwind:
        headers.append(Script(src="https://cdn.tailwindcss.com"))

    if include_lucide:
        headers.append(Script(src="https://unpkg.com/lucide@latest"))

    # EidosUI CSS
    for css_url in get_css_urls():
        headers.append(Link(rel="stylesheet", href=css_url))

    # EidosUI JavaScript
    if include_eidos_js:
        headers.append(Script(src="/eidos/js/eidos.js", defer=True))

    # Initialization script
    init_script = f"""
        // Set theme
        document.documentElement.setAttribute('data-theme', '{theme}');
    """

    if include_lucide:
        init_script += """
        // Initialize Lucide icons
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                if (window.lucide) lucide.createIcons();
            });
        } else {
            if (window.lucide) lucide.createIcons();
        }
    """

    headers.append(Script(init_script))

    return headers
