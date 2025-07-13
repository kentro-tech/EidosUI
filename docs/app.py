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


def layout(title, navigation, *content):
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
                }
                .sidebar-nav a {
                    display: block;
                    padding: 0.5rem 1rem;
                    border-radius: 0.375rem;
                    transition: all 150ms;
                }
                .sidebar-nav a:hover {
                    background: var(--eidos-bg-secondary);
                }
                .sidebar-nav a.active {
                    background: var(--eidos-primary);
                    color: var(--eidos-primary-text);
                }
                @media (max-width: 1024px) {
                    .sidebar-nav {
                        display: none;
                    }
                }
            """)
        ),
        Body(
            navigation,
            Div(
                # Sidebar navigation
                Aside(
                    Nav(
                        H3("Documentation", class_="px-4 mb-4 text-sm font-semibold uppercase"),
                        A("Introduction", href="/", class_="active" if title == "Introduction" else ""),
                        # A("Getting Started", href="/getting-started", class_="active" if title == "Getting Started" else ""),
                        A("Kitchen Sink", href="/kitchen-sink", class_="active" if title == "Kitchen Sink" else ""),
                        # A("Styling", href="/styling", class_="active" if title == "Styling" else ""),
                        # A("Philosophy", href="/philosophy", class_="active" if title == "Philosophy" else ""),
                        
                        # H3("Plugins", class_="px-4 mt-6 mb-4 text-sm font-semibold uppercase"),
                        # A("Plugin System", href="/plugins", class_="active" if title == "Plugins" else ""),
                        # A("Markdown Plugin", href="/plugins/markdown", class_="active" if title == "Markdown Plugin" else ""),
                        # A("Creating Extensions", href="/plugins/markdown-extensions", class_="active" if title == "Markdown Extensions" else ""),
                        
                        H3("Meta", class_="px-4 mt-6 mb-4 text-sm font-semibold uppercase"),
                        A("About", href="/about", class_="active" if title == "About" else ""),
                        
                        H3("API Reference", class_="px-4 mt-6 mb-4 text-sm font-semibold uppercase"),
                        A("API Index", href="/api", class_="active" if title == "API Reference" else ""),
                        
                        class_="sidebar-nav"
                    ),
                    class_="hidden lg:block w-64 pr-8"
                ),
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


def create_nav():
    """Create the main navigation bar"""
    return NavBar(
        A("Docs", href="/"),
        A("Kitchen Sink", href="/kitchen-sink"),
        A("GitHub", href="https://github.com/isaac-flath/EidosUI", target="_blank"),
        Button(
            "🌙",
            class_="theme-toggle p-2 rounded-full",
        ),
        lcontents=H3("EidosUI", class_="text-xl font-bold"),
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
        create_nav(),
        load_markdown("index.md")
    )

@app.get("/kitchen-sink")
def kitchen_sink():
    """Kitchen Sink showcase"""
    return layout(
        "Kitchen Sink of all EidosUI components",
        create_nav(),
        components_page()
    )

@app.get("/about")
def about():
    """About page"""
    return layout(
        "About",
        create_nav(),
        load_markdown("about.md")
    )


@app.get("/api")
def api_index():
    """API Reference index"""
    modules = get_available_modules()
    return layout(
        "API Reference",
        create_nav(),
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
        create_nav(),
        render_api_page(api_data)
    )
