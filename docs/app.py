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
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style("""
                /* Mobile-first approach */
                .sidebar-nav {
                    display: block !important;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 280px;
                    height: 100vh;
                    background: var(--color-background);
                    border-right: 1px solid var(--color-border);
                    padding: 5rem 1rem 2rem 1rem;
                    overflow-y: auto;
                    z-index: 40;
                    transform: translateX(-100%);
                    transition: transform 0.3s ease;
                }
                
                .sidebar-nav.mobile-open {
                    transform: translateX(0);
                }
                
                .sidebar-overlay {
                    display: none;
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.5);
                    z-index: 30;
                }
                
                .sidebar-overlay.active {
                    display: block;
                }
                
                .mobile-menu-btn {
                    display: block;
                }
                
                .main-content {
                    width: 100%;
                    padding: 1rem;
                }
                
                /* Desktop styles */
                @media (min-width: 768px) {
                    .sidebar-nav {
                        display: block;
                        position: sticky;
                        top: 5rem;
                        left: auto;
                        width: 250px;
                        height: calc(100vh - 6rem);
                        transform: none;
                        border-right: none;
                        padding: 0 2rem 2rem 0;
                        z-index: 1;
                    }
                    
                    .sidebar-overlay {
                        display: none !important;
                    }
                    
                    .mobile-menu-btn {
                        display: none;
                    }
                    
                    .main-content {
                        flex: 1;
                        max-width: 60rem;
                        padding: 0;
                    }
                    
                    .content-wrapper {
                        display: flex;
                        gap: 2rem;
                    }
                }
                
                /* Sidebar styles */
                .sidebar-nav a {
                    display: block;
                    padding: 0.375rem 1rem;
                    border-radius: 0.375rem;
                    transition: all 150ms;
                    color: var(--color-text-muted);
                    text-decoration: none;
                    font-size: 0.875rem;
                    margin: 0.125rem 0;
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
                    margin: 0 0 1rem 0;
                    color: var(--color-text);
                    font-size: 0.875rem;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                }
                .sidebar-nav > div {
                    margin-bottom: 0.5rem;
                }
                .sidebar-nav span {
                    text-transform: capitalize;
                }
                
                /* Close button for mobile */
                .sidebar-close {
                    position: absolute;
                    top: 1rem;
                    right: 1rem;
                    background: none;
                    border: none;
                    font-size: 1.5rem;
                    cursor: pointer;
                    color: var(--color-text-muted);
                    display: block;
                }
                
                @media (min-width: 768px) {
                    .sidebar-close {
                        display: none;
                    }
                }
            """)
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("Quick Start", href="/quick-start", class_="hidden sm:block"),
                A("Kitchen Sink", href="/kitchen-sink", class_="hidden sm:block"),
                A("Concepts", href="/concepts", class_="hidden sm:block"),
                A("Reference", href="/api"),
                A("Plugins", href="/plugins", class_="hidden sm:block"),
                Button(
                    "☀️",  # Default to sun icon
                    class_="theme-toggle p-2 rounded-full",
                    id="theme-toggle"
                ),
                lcontents=Div(
                    (
                        Button(
                            "☰",
                            class_="mobile-menu-btn p-2 rounded text-xl mr-2",
                            id="mobile-menu-btn",
                            style="background: none; border: none; cursor: pointer; color: var(--color-text);"
                        ) if sidebar else ""
                    ),
                    H3("EidosUI", class_="text-xl font-bold"),
                    class_="flex items-center"
                ),
                sticky=True
            ),
            # Sidebar overlay for mobile (only if sidebar exists)
            (Div(class_="sidebar-overlay", id="sidebar-overlay") if sidebar else ""),
            # Content wrapper
            Div(
                # Sidebar with close button
                (
                    Div(
                        Button("✕", class_="sidebar-close", id="sidebar-close"),
                        sidebar,
                        class_="sidebar-nav",
                        id="sidebar-nav"
                    ) if sidebar else ""
                ),
                # Main content
                Main(
                    *content,
                    class_="main-content"
                ),
                class_="container mx-auto px-4 sm:px-6 py-4 sm:py-8 content-wrapper"
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
                
                // Mobile menu handling
                const mobileMenuBtn = document.getElementById('mobile-menu-btn');
                const sidebarNav = document.getElementById('sidebar-nav');
                const sidebarOverlay = document.getElementById('sidebar-overlay');
                const sidebarClose = document.getElementById('sidebar-close');
                
                function openSidebar() {
                    if (sidebarNav) {
                        sidebarNav.classList.add('mobile-open');
                        sidebarOverlay.classList.add('active');
                        document.body.style.overflow = 'hidden';
                    }
                }
                
                function closeSidebar() {
                    if (sidebarNav) {
                        sidebarNav.classList.remove('mobile-open');
                        sidebarOverlay.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                }
                
                if (mobileMenuBtn) {
                    mobileMenuBtn.onclick = openSidebar;
                }
                
                if (sidebarClose) {
                    sidebarClose.onclick = closeSidebar;
                }
                
                if (sidebarOverlay) {
                    sidebarOverlay.onclick = closeSidebar;
                }
                
                // Close sidebar on navigation (mobile)
                if (sidebarNav) {
                    sidebarNav.querySelectorAll('a').forEach(link => {
                        link.addEventListener('click', () => {
                            if (window.innerWidth < 768) {
                                closeSidebar();
                            }
                        });
                    });
                }
                
                // Mark active sidebar link
                const path = window.location.pathname;
                document.querySelectorAll('.sidebar-nav a').forEach(link => {
                    if (link.getAttribute('href') === path) link.classList.add('active');
                });
            """)
        )
    )


def create_api_sidebar(modules, current_module=None):
    """Create a sidebar for API navigation with directory structure"""
    # Build a tree structure from the modules
    tree = {}
    for module in modules:
        # Remove 'eidos.' prefix for cleaner display
        clean_name = module.replace('eidos.', '')
        parts = clean_name.split('.')
        
        # Build nested structure
        current = tree
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                # Leaf node - store the full module name
                current[part] = module
            else:
                # Directory node
                if part not in current:
                    current[part] = {}
                current = current[part]
    
    def render_tree(node, prefix=""):
        items = []
        
        # Sort items: directories first, then files
        sorted_items = sorted(node.items(), key=lambda x: (isinstance(x[1], str), x[0]))
        
        for name, value in sorted_items:
            if isinstance(value, str):
                # It's a module (leaf node)
                is_active = value == current_module
                items.append(
                    A(
                        name,
                        href=f"/api/{value}",
                        class_="active" if is_active else "",
                        style=f"padding-left: {len(prefix) * 1.5 + 1}rem;"
                    )
                )
            else:
                # It's a directory (branch node)
                items.append(
                    Div(
                        Span(name, style=f"font-weight: 600; display: block; padding: 0.5rem 0 0.25rem {len(prefix) * 1.5}rem; color: var(--color-text); font-size: 0.875rem;"),
                        *render_tree(value, prefix + "  ")
                    )
                )
        
        return items
    
    sidebar_content = [
        H4("API Reference"),
        *render_tree(tree)
    ]
    
    return Div(*sidebar_content)


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