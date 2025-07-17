"""EidosUI Documentation - A runnable documentation app built with EidosUI"""

from pathlib import Path

import air
from air.tags import *
from api_extractor import extract_module_api, get_available_modules
from api_renderer import render_api_index, render_api_page
from kitchen_sink import components_page

from eidos.components.headers import EidosHeaders
from eidos.components.navigation import NavBar
from eidos.components.tabs import TabList, TabPanel
from eidos.plugins.markdown import Markdown, MarkdownCSS
from eidos.tags import *
from eidos.utils import get_eidos_static_files

app = air.Air()

from fastapi.staticfiles import StaticFiles

for mount_path, directory in get_eidos_static_files(markdown=True).items():
    app.mount(
        mount_path,
        StaticFiles(directory=directory),
        name=mount_path.strip("/").replace("/", "_"),
    )

# Get the docs directory
DOCS_DIR = Path(__file__).parent


def layout(title, *content, sidebar=None):
    """Shared layout for all documentation pages"""
    return Html(
        Head(
            *EidosHeaders(),
            MarkdownCSS(),
            Title(f"{title} - EidosUI Docs"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org@1.9.10"),

            Script("""
                // Immediately set theme to prevent flash
                (function() {
                    const THEME_KEY = 'eidos-theme-preference';
                    const savedTheme = localStorage.getItem(THEME_KEY);
                    const theme = (savedTheme === 'light' || savedTheme === 'dark') 
                        ? savedTheme 
                        : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
                    document.documentElement.setAttribute('data-theme', theme);
                })();
            """),
            Style("""
                .docs-sidebar {
                    background: var(--color-surface);
                    border-radius: 0.5rem;
                    padding: 1rem;
                    margin-bottom: 2rem;
                }

                @media (min-width: 768px) {
                    .docs-sidebar {
                        position: sticky;
                        top: 5rem;
                        height: fit-content;
                        max-height: calc(100vh - 6rem);
                        overflow-y: auto;
                        margin-bottom: 0;
                        min-width: 250px;
                    }

                    .docs-layout {
                        display: flex;
                        gap: 2rem;
                    }

                    .docs-content {
                        flex: 1;
                        max-width: 60rem;
                    }
                }

                /* Collapsible on mobile only */
                @media (max-width: 767px) {
                    .docs-sidebar[data-collapsed="true"] .sidebar-content {
                        display: none;
                    }
                }

                .sidebar-toggle {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    width: 100%;
                    padding: 0.5rem;
                    margin: -0.5rem -0.5rem 0.5rem -0.5rem;
                    cursor: pointer;
                    color: var(--color-text);
                    border-radius: 0.25rem;
                }

                .sidebar-toggle:hover {
                    background: var(--color-background);
                }

                @media (min-width: 768px) {
                    .sidebar-toggle {
                        display: none;
                    }
                }

                /* Sidebar links */
                .docs-sidebar a {
                    display: block;
                    padding: 0.375rem 0.75rem;
                    border-radius: 0.375rem;
                    color: var(--color-text-muted);
                    text-decoration: none;
                    font-size: 0.875rem;
                    margin: 0.125rem 0;
                    transition: all 150ms;
                }

                .docs-sidebar a:hover {
                    background: var(--color-background);
                    color: var(--color-text);
                }

                .docs-sidebar a.active {
                    background: var(--color-primary-light);
                    color: var(--color-primary);
                    font-weight: 500;
                }

                .docs-sidebar h4 {
                    font-size: 0.875rem;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    color: var(--color-text);
                    margin: 1rem 0 0.5rem 0;
                }

                .docs-sidebar > div {
                    margin-bottom: 0.5rem;
                }

                .docs-sidebar span {
                    font-weight: 600;
                    display: block;
                    padding: 0.5rem 0 0.25rem 0;
                    color: var(--color-text);
                    font-size: 0.875rem;
                    text-transform: capitalize;
                }
            """),
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("Quick Start", href="/quick-start"),
                A("Kitchen Sink", href="/kitchen-sink"),
                A("Concepts", href="/concepts"),
                A("Reference", href="/api"),
                A("Plugins", href="/plugins", class_="hidden sm:block"),
                Button("☀️", class_="theme-toggle p-2 rounded-full", id="theme-toggle"),
                lcontents=H3("EidosUI", class_="text-xl font-bold"),
                sticky=True,
            ),
            Div(
                Div(
                    sidebar if sidebar else "",
                    Main(*content, class_="docs-content"),
                    class_="docs-layout",
                )
                if sidebar
                else Main(*content),
                class_="container mx-auto px-4 sm:px-6 py-4 sm:py-8",
            ),
            Script("""
                // Theme management
                const THEME_KEY = 'eidos-theme-preference';
                function getTheme() {
                    const t = localStorage.getItem(THEME_KEY);
                    if (t === 'light' || t === 'dark') return t;
                    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
                }
                function setTheme(theme) {
                    document.documentElement.setAttribute('data-theme', theme);
                    localStorage.setItem(THEME_KEY, theme);
                    const btn = document.getElementById('theme-toggle');
                    if (btn) btn.textContent = theme === 'dark' ? '☀️' : '🌙';
                }
                setTheme(getTheme());
                const btn = document.getElementById('theme-toggle');
                if (btn) btn.onclick = () => {
                    const t = document.documentElement.getAttribute('data-theme');
                    setTheme(t === 'dark' ? 'light' : 'dark');
                };

                // Mobile sidebar toggle
                const sidebarToggle = document.querySelector('.sidebar-toggle');
                const sidebar = document.querySelector('.docs-sidebar');
                if (sidebarToggle && sidebar) {
                    // Start collapsed on mobile
                    if (window.innerWidth < 768) {
                        sidebar.setAttribute('data-collapsed', 'true');
                    }

                    sidebarToggle.onclick = () => {
                        const isCollapsed = sidebar.getAttribute('data-collapsed') === 'true';
                        sidebar.setAttribute('data-collapsed', !isCollapsed);
                        const icon = sidebarToggle.querySelector('[data-lucide]');
                        if (icon) {
                            icon.setAttribute('data-lucide', isCollapsed ? 'chevron-down' : 'chevron-right');
                            lucide.createIcons();
                        }
                    };

                    // Handle window resize
                    let resizeTimer;
                    window.addEventListener('resize', () => {
                        clearTimeout(resizeTimer);
                        resizeTimer = setTimeout(() => {
                            if (window.innerWidth >= 768) {
                                // Always expand on desktop
                                sidebar.setAttribute('data-collapsed', 'false');
                            }
                        }, 150);
                    });
                }

                // Mark active link
                const path = window.location.pathname;
                document.querySelectorAll('.docs-sidebar a').forEach(link => {
                    if (link.getAttribute('href') === path) link.classList.add('active');
                });
            """),
        ),
    )


def create_api_sidebar(modules, current_module=None):
    """Create a simple sidebar for API navigation"""
    # Build tree structure
    tree = {}
    for module in modules:
        clean_name = module.replace("eidos.", "")
        parts = clean_name.split(".")

        current = tree
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                current[part] = module
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]

    def render_tree(node, indent=0):
        items = []
        sorted_items = sorted(node.items(), key=lambda x: (isinstance(x[1], str), x[0]))

        for name, value in sorted_items:
            if isinstance(value, str):
                # Module link
                items.append(
                    A(
                        name,
                        href=f"/api/{value}",
                        style=f"padding-left: {indent + 0.75}rem;",
                    )
                )
            else:
                # Section header
                items.append(Span(name, style=f"padding-left: {indent}rem;"))
                items.extend(render_tree(value, indent + 2))

        return items

    return Div(
        Button(
            Span("API Reference"),
            I(data_lucide="chevron-down", class_="w-4 h-4"),
            class_="sidebar-toggle md:hidden",
        ),
        Div(
            H4("API Reference", class_="hidden md:block"),
            *render_tree(tree),
            class_="sidebar-content",
        ),
        class_="docs-sidebar",
    )


def load_markdown(filename):
    """Load and render a markdown file"""
    filepath = DOCS_DIR / filename
    if filepath.exists():
        with open(filepath) as f:
            return Markdown(f.read())
    return P("Documentation file not found.", class_="text-red-500")


@app.get("/")
def home():
    """Documentation homepage"""
    return layout("Introduction", load_markdown("index.md"))


@app.get("/quick-start")
def quick_start():
    """Quick Start page"""
    return layout("Quick Start", load_markdown("quick-start.md"))


@app.get("/kitchen-sink")
def kitchen_sink():
    """Kitchen Sink showcase"""
    return layout("Kitchen Sink of all EidosUI components", components_page())


@app.get("/about")
def about():
    """About page"""
    return layout("About", load_markdown("about.md"))


@app.get("/concepts")
def concepts():
    """Concepts page"""
    return layout("Concepts", load_markdown("concepts/index.md"))


@app.get("/concepts/{concept_name:path}")
def concept_detail(concept_name: str):
    """Concept detail page"""
    return layout(f"Concept: {concept_name}", load_markdown(f"concepts/{concept_name}.md"))


@app.get("/api")
def api_index():
    """API Reference index"""
    modules = get_available_modules()
    return layout("API Reference", render_api_index(modules), sidebar=create_api_sidebar(modules))


@app.get("/api/{module_path:path}")
def api_module(module_path: str):
    """API Reference for a specific module"""
    # Convert URL path to module path
    module_name = module_path.replace("/", ".")
    modules = get_available_modules()

    api_data = extract_module_api(module_name)
    return layout(
        f"API: {module_name}",
        render_api_page(api_data),
        sidebar=create_api_sidebar(modules, module_name),
    )


@app.get("/plugins")
def plugins():
    """Plugins page"""
    return layout("Plugins", load_markdown("plugins/index.md"))


@app.get("/plugins/{plugin_name:path}")
def plugin_detail(plugin_name: str):
    """Plugin detail page"""
    return layout(f"Plugin: {plugin_name}", load_markdown(f"plugins/{plugin_name}.md"))


# Tab example routes - these need to be prefixed with /tab/ to match the pattern
@app.get("/tab/typography")
def tab_typography():
    """Typography tab with semantic HTML examples"""
    # Return BOTH the tab list and content together
    return Div(
        TabList(
            ("Typography", "/tab/typography"),
            ("Lists", "/tab/lists"),
            ("Code", "/tab/code"),
            selected=0,
            hx_target="#demo-tabs",
        ),
        TabPanel(
            Div(
                H3("Typography Examples"),
                P(
                    "This tab demonstrates various ",
                    Strong("semantic HTML elements"),
                    " for text formatting."
                ),

                H4("Text Emphasis"),
                P(
                    "You can use ",
                    Strong("strong"),
                    " for importance, ",
                    Em("emphasis"),
                    " for stress, and ",
                    Mark("mark"),
                    " for highlighting."
                ),

                H4("Quotations"),
                Blockquote(
                    "The Web is the ultimate customer-empowering environment. "
                    "He or she who clicks the mouse gets to decide everything.",
                    Cite("— Jakob Nielsen")
                ),

                H4("Abbreviations and Time"),
                P(
                    "The ",
                    Abbr("W3C", title="World Wide Web Consortium"),
                    " was founded in ",
                    Time("October 1994", datetime="1994-10"),
                    "."
                ),

                H4("Deleted and Inserted Text"),
                P(
                    "Prices have been ",
                    Del("increased"),
                    " ",
                    Ins("reduced"),
                    " for the holiday season!"
                ),

                class_="space-y-4"
            )
        )
    )


@app.get("/tab/lists")
def tab_lists():
    """Lists tab with various list examples"""
    return Div(
        TabList(
            ("Typography", "/tab/typography"),
            ("Lists", "/tab/lists"),
            ("Code", "/tab/code"),
            selected=1,
            hx_target="#demo-tabs",
        ),
        TabPanel(
            Div(
                H3("List Examples"),

                H4("Unordered List"),
                Ul(
                    Li("First item with simple text"),
                    Li(Strong("Second item"), " with strong emphasis"),
                    Li("Third item with ", Code("inline code")),
                    Li(
                        "Fourth item with nested list:",
                        Ul(
                            Li("Nested item 1"),
                            Li("Nested item 2"),
                            Li("Nested item 3")
                        )
                    )
                ),

                H4("Ordered List"),
                Ol(
                    Li("Install EidosUI: ", Code("pip install eidos")),
                    Li("Import components: ", Code("from eidos.components import *")),
                    Li("Build your UI with semantic HTML"),
                    Li("Deploy your application")
                ),

                H4("Definition List"),
                Dl(
                    Dt("HTML"),
                    Dd("HyperText Markup Language - the standard markup language for documents designed to be displayed in a web browser"),

                    Dt("CSS"),
                    Dd("Cascading Style Sheets - a style sheet language used for describing the presentation of a document"),

                    Dt("JavaScript"),
                    Dd("A programming language that conforms to the ECMAScript specification"),
                ),

                class_="space-y-4"
            )
        )
    )


@app.get("/tab/code")
def tab_code():
    """Code tab with code-related semantic elements"""
    return Div(
        TabList(
            ("Typography", "/tab/typography"),
            ("Lists", "/tab/lists"),
            ("Code", "/tab/code"),
            selected=2,
            hx_target="#demo-tabs",
        ),
        TabPanel(
            Div(
                H3("Code Examples"),

                H4("Inline Code Elements"),
                P(
                    "Use ",
                    Code("code"),
                    " for inline code, ",
                    Kbd("Ctrl+C"),
                    " for keyboard input, ",
                    Var("x"),
                    " for variables, and ",
                    Samp("Hello World"),
                    " for sample output."
                ),

                H4("Code Block"),
                Pre('''def handle_tab_route():
    """Return tab list + content together"""
    return Div(
        TabList(
            ("Tab 1", "/tab1"),
            ("Tab 2", "/tab2"),
            selected=0,
            hx_target="#tabs"
        ),
        TabPanel(content)
    )'''),

                H4("Shell Commands"),
                P("To install EidosUI, run:"),
                Pre("$ pip install eidos\n$ python -m eidos.cli init"),

                H4("Keyboard Shortcuts"),
                P(
                    "Common shortcuts: ",
                    Kbd("Cmd+S"),
                    " to save, ",
                    Kbd("Cmd+Z"),
                    " to undo, ",
                    Kbd("Cmd+Shift+Z"),
                    " to redo."
                ),

                Details(
                    Summary("HTMX Tab Implementation"),
                    Pre('''# Initial container on main page
TabContainer("/tab/typography", target_id="demo-tabs")

# Each tab route returns the complete structure
@app.get("/tab/typography")
def tab_typography():
    return Div(
        TabList(
            ("Typography", "/tab/typography"),
            ("Lists", "/tab/lists"),
            ("Code", "/tab/code"),
            selected=0,
            hx_target="#demo-tabs"
        ),
        TabPanel(
            # Tab content here
        )
    )'''),
                    class_="mt-4"
                ),

                class_="space-y-4"
            )
        )
    )
