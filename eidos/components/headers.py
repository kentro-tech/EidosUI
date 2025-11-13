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
    include_theme_switcher: bool = True,
) -> list[Tag]:
    """Complete EidosUI headers with EidosUI JavaScript support.

    Args:
        include_tailwind: Include Tailwind CSS CDN
        include_lucide: Include Lucide Icons CDN
        include_eidos_js: Include EidosUI JavaScript (navigation, future features)
        include_theme_switcher: Include theme switching functionality
    """
    headers = [
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    ]

    # Theme init (before other scripts to prevent FOUC)
    if include_theme_switcher:
        headers.append(
            Script("""
(function() {
    const saved = localStorage.getItem('eidos-theme-preference');
    const theme = (saved === 'light' || saved === 'dark')
        ? saved
        : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
})();
""")
        )

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

    # Theme switcher
    if include_theme_switcher:
        headers.append(Script(src="/eidos/js/theme.js", defer=True))

    # Lucide initialization
    if include_lucide:
        headers.append(
            Script("""
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        if (window.lucide) lucide.createIcons();
    });
} else {
    if (window.lucide) lucide.createIcons();
}
""")
        )

    return headers
