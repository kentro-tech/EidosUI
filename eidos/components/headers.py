from typing import Literal, Optional

from air import Link, Meta, Script, Tag
from airpine import RawJS


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
    include_alpine: bool = True,
    include_eidos_js: bool = True,
    include_theme_switcher: bool = True,
    force_theme: Optional[Literal["light", "dark"]] = None,
) -> list[Tag]:
    """Complete EidosUI headers with EidosUI JavaScript support.

    Args:
        include_tailwind: Include Tailwind CSS CDN
        include_lucide: Include Lucide Icons CDN
        include_alpine: Include Alpine.js CDN
        include_eidos_js: Include EidosUI JavaScript (navigation, future features)
        include_theme_switcher: Include theme switching functionality
        force_theme: Force a specific theme ("light" or "dark"), ignoring user preference
    """
    headers = [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    ]

    # Theme init (before other scripts to prevent FOUC)
    if force_theme:
        theme_init = RawJS(f"""
(function() {{
    document.documentElement.setAttribute('data-theme', '{force_theme}');
}})()
""")
        headers.append(Script(str(theme_init)))
    elif include_theme_switcher:
        theme_init = RawJS("""
(function() {
    const saved = localStorage.getItem('eidos-theme-preference');
    const theme = (saved === 'light' || saved === 'dark')
        ? saved
        : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
})()
""")
        headers.append(Script(str(theme_init)))

    # Core libraries
    if include_tailwind:
        headers.append(Script(src="https://cdn.tailwindcss.com"))

    if include_lucide:
        headers.append(Script(src="https://unpkg.com/lucide@latest"))

    # EidosUI CSS
    for css_url in get_css_urls():
        headers.append(Link(rel="stylesheet", href=css_url))

    # Theme switcher (before Alpine)
    if include_theme_switcher:
        headers.append(Script(src="/eidos/js/theme.js", defer=True))

    # EidosUI JavaScript (before Alpine)
    if include_eidos_js:
        headers.append(Script(src="/eidos/js/eidos.js", defer=True))

    # Alpine.js (must load after theme.js and eidos.js)
    if include_alpine:
        headers.append(
            Script(
                src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js",
                defer=True,
            )
        )

    # Lucide initialization
    if include_lucide:
        lucide_init = RawJS("""
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        if (window.lucide) lucide.createIcons();
    });
} else {
    if (window.lucide) lucide.createIcons();
}
""")
        headers.append(Script(str(lucide_init)))

    return headers
