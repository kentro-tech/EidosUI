"""EidosUI Documentation - A runnable documentation app built with EidosUI"""

import air
from air.tags import *
from eidos.tags import *
from eidos.components.navigation import NavBar
import eidos.styles as styles
from eidos.components.headers import EidosHeaders
from eidos.utils import get_eidos_static_directory
from eidos.plugins.markdown import Markdown, MarkdownCSS
from pathlib import Path
from kitchen_sink import components_page
from api_extractor import extract_module_api, get_available_modules
from api_renderer import render_api_page, render_api_index

app = air.Air()

from fastapi.staticfiles import StaticFiles

# Mount static files for CSS
app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")

# Get the docs directory
DOCS_DIR = Path(__file__).parent


def layout(title, *content, sidebar=None):
    """Shared layout for all documentation pages"""
    return Html(
        Head(
            *EidosHeaders(),
            MarkdownCSS(),
            Title(f"{title} - EidosUI Docs"),
            Style("""
                .sidebar-nav {
                    position: sticky;
                    top: 5rem;
                    height: calc(100vh - 6rem);
                    overflow-y: auto;
                    min-width: 200px;
                    padding-right: 2rem;
                }
                .sidebar-nav a {
                    display: block;
                    padding: 0.5rem 1rem;
                    border-radius: 0.375rem;
                    transition: all 150ms;
                    color: var(--color-text-muted);
                    text-decoration: none;
                    font-size: 0.875rem;
                }
                .sidebar-nav a:hover {
                    background: var(--color-surface);
                    color: var(--color-text);
                }
                .sidebar-nav a.active {
                    background: var(--color-primary-light);
                    color: var(--color-primary);
                    font-weight: 500;
                }
                .sidebar-nav h4 {
                    font-weight: 600;
                    margin: 1rem 0 0.5rem 0;
                    color: var(--color-text);
                    font-size: 0.75rem;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                }
            """)
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("Quick Start", href="/quick-start"),
                A("Kitchen Sink", href="/kitchen-sink"),
                A("Concepts", href="/concepts"),
                A("Reference", href="/api"),
                A("Plugins", href="/plugins"),
                Button(
                    "☀️",  # Default to sun icon
                    class_="theme-toggle p-2 rounded-full",
                    id="theme-toggle"
                ),
                lcontents=H3("EidosUI", class_="text-xl font-bold"),
                sticky=True
            ),
            Div(
                # Sidebar if provided
                sidebar if sidebar else "",
                # Main content
                Main(
                    *content,
                    class_="flex-1"
                ),
                class_="container mx-auto px-6 py-8 flex gap-8"
            ),
            Script("""
                // Theme management with persistence and system preference support
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
                window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
                    if (!localStorage.getItem(THEME_KEY)) setTheme(e.matches ? 'dark' : 'light');
                });
                const path = window.location.pathname;
                document.querySelectorAll('.sidebar-nav a').forEach(link => {
                    if (link.getAttribute('href') === path) link.classList.add('active');
                });
            """)
        )
    )


def create_api_sidebar(modules, current_module=None):
    """Create a sidebar for API navigation"""
    items = [H4("API Modules")]
    
    for module in sorted(modules):
        is_active = module == current_module
        items.append(
            A(
                module, 
                href=f"/api/{module}",
                class_="active" if is_active else ""
            )
        )
    
    return Div(*items, class_="sidebar-nav")


def load_markdown(filename):
    """Load and render a markdown file"""
    filepath = DOCS_DIR / filename
    if filepath.exists():
        with open(filepath, 'r') as f:
            return Markdown(f.read())
    return P("Documentation file not found.", class_="text-red-500")

@app.get("/")
def home():
    """Documentation homepage"""
    return layout(
        "Introduction",
        load_markdown("index.md")
    )

@app.get("/quick-start")
def quick_start():
    """Quick Start page"""
    return layout(
        "Quick Start",
        load_markdown("quick-start.md")
    )

@app.get("/kitchen-sink")
def kitchen_sink():
    """Kitchen Sink showcase"""
    return layout(
        "Kitchen Sink of all EidosUI components",
        components_page()
    )

@app.get("/about")
def about():
    """About page"""
    return layout(
        "About",
        load_markdown("about.md")
    )

@app.get("/concepts")
def concepts():
    """Concepts page"""
    return layout(
        "Concepts",
        load_markdown("concepts/index.md")
    )

@app.get("/concepts/{concept_name:path}")
def concept_detail(concept_name: str):
    """Concept detail page"""
    return layout(
        f"Concept: {concept_name}",
        load_markdown(f"concepts/{concept_name}.md")
    )

@app.get("/api")
def api_index():
    """API Reference index"""
    modules = get_available_modules()
    return layout(
        "API Reference",
        render_api_index(modules),
        sidebar=create_api_sidebar(modules)
    )


@app.get("/api/{module_path:path}")
def api_module(module_path: str):
    """API Reference for a specific module"""
    # Convert URL path to module path (e.g., "eidos/tags" -> "eidos.tags")
    module_name = module_path.replace('/', '.')
    modules = get_available_modules()
    
    api_data = extract_module_api(module_name)
    return layout(
        f"API: {module_name}",
        render_api_page(api_data),
        sidebar=create_api_sidebar(modules, module_name)
    )

@app.get("/plugins")
def plugins():
    """Plugins page"""
    return layout(
        "Plugins",
        load_markdown("plugins/index.md")
    )

@app.get("/plugins/{plugin_name:path}")
def plugin_detail(plugin_name: str):
    """Plugin detail page"""
    return layout(
        f"Plugin: {plugin_name}",
        load_markdown(f"plugins/{plugin_name}.md")
    )