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


def layout(title, *content):
    """Shared layout for all documentation pages"""
    return Html(
        Head(
            *EidosHeaders(),
            MarkdownCSS(),
            Title(f"{title} - EidosUI Docs"),
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
                    "🌙",
                    class_="theme-toggle p-2 rounded-full",
                ),
                lcontents=H3("EidosUI", class_="text-xl font-bold"),
                sticky=True
            ),
            Div(
                # Main content
                Main(
                    *content,
                    class_="flex-1"
                ),
                class_="container mx-auto px-6 py-8 flex gap-8"
            ),
            Script("""
                const toggles = document.querySelectorAll('.theme-toggle');
                toggles.forEach(toggle => {
                    toggle.addEventListener('click', () => {
                        const html = document.documentElement;
                        const currentTheme = html.getAttribute('data-theme');
                        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        html.setAttribute('data-theme', newTheme);
                        toggles.forEach(btn => {
                            btn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
                        });
                    });
                });
            """)
        )
    )


def create_sidebar(items: dict[str, str]):
    """Create a nested sidebar with the given items and subitems"""
    return Sidebar(
        *[A(item, href=items[item]) for item in items],
        class_="sidebar-nav",
        sticky=True
    )


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
        render_api_index(modules)
    )


@app.get("/api/{module_path:path}")
def api_module(module_path: str):
    """API Reference for a specific module"""
    # Convert URL path to module path (e.g., "eidos/tags" -> "eidos.tags")
    module_name = module_path.replace('/', '.')
    
    api_data = extract_module_api(module_name)
    return layout(
        f"API: {module_name}",
        render_api_page(api_data)
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