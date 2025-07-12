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
                        A("Getting Started", href="/getting-started", class_="active" if title == "Getting Started" else ""),
                        A("Kitchen Sink", href="/kitchen-sink", class_="active" if title == "Kitchen Sink" else ""),
                        A("Styling", href="/styling", class_="active" if title == "Styling" else ""),
                        A("Philosophy", href="/philosophy", class_="active" if title == "Philosophy" else ""),
                        
                        H3("Plugins", class_="px-4 mt-6 mb-4 text-sm font-semibold uppercase"),
                        A("Plugin System", href="/plugins", class_="active" if title == "Plugins" else ""),
                        A("Markdown Plugin", href="/plugins/markdown", class_="active" if title == "Markdown Plugin" else ""),
                        A("Creating Extensions", href="/plugins/markdown-extensions", class_="active" if title == "Markdown Extensions" else ""),
                        
                        H3("Meta", class_="px-4 mt-6 mb-4 text-sm font-semibold uppercase"),
                        A("About", href="/about", class_="active" if title == "About" else ""),
                        
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


@app.get("/getting-started")
def getting_started():
    """Getting started guide"""
    return layout(
        "Getting Started",
        create_nav(),
        load_markdown("getting-started.md")
    )


@app.get("/kitchen-sink")
def kitchen_sink():
    """Kitchen Sink showcase"""
    return layout(
        "Kitchen Sink of all EidosUI components",
        create_nav(),
        components_page()
    )


@app.get("/styling")
def styling():
    """Styling system documentation"""
    return layout(
        "Styling",
        create_nav(),
        load_markdown("styling.md")
    )


@app.get("/philosophy")
def philosophy():
    """Philosophy and architecture"""
    return layout(
        "Philosophy",
        create_nav(),
        load_markdown("philosophy.md")
    )


@app.get("/plugins")
def plugins():
    """Plugin system overview"""
    return layout(
        "Plugins",
        create_nav(),
        load_markdown("plugins/index.md")
    )


@app.get("/plugins/markdown")
def plugins_markdown():
    """Markdown plugin documentation"""
    return layout(
        "Markdown Plugin",
        create_nav(),
        load_markdown("plugins/markdown.md")
    )


@app.get("/plugins/markdown-extensions")
def plugins_markdown_extensions():
    """Markdown extension guide"""
    return layout(
        "Markdown Extensions",
        create_nav(),
        load_markdown("plugins/markdown-extension-guide.md")
    )


@app.get("/about")
def about():
    """About page"""
    return layout(
        "About",
        create_nav(),
        Article(
            H1("About"),
            
            Section(
                H2("Purpose"),
                P("EidosUI fills the gap between rapid prototyping and custom design."),
                P("MonsterUI: Fast development, opinionated defaults."),
                P("EidosUI: Flexible customization, exposed building blocks."),
                P("Raw Tailwind: Complete control, no components.")
            ),
            
            Section(
                H2("Background"),
                
                H3("Related Projects"),
                Ul(
                    Li(A("FastHTML", href="https://fastht.ml", target="_blank"), " - Python web framework"),
                    Li(A("MonsterUI", href="https://github.com/isaac-flath/MonsterUI", target="_blank"), " - Rapid UI development")
                ),
                
                H3("Key Influences"),
                Ul(
                    Li("Tailwind CSS - Utility-first styling"),
                    Li("CSS Variables - Runtime theming"),
                    Li("Semantic HTML - Meaningful markup")
                )
            ),
            
            Section(
                H2("When to Use"),
                
                Div(
                    H3("MonsterUI"),
                    Ul(
                        Li("Rapid prototyping"),
                        Li("Default styling acceptable"),
                        Li("Internal tools"),
                        Li("Maximum convenience")
                    ),
                    class_="mb-6"
                ),
                
                Div(
                    H3("EidosUI"),
                    Ul(
                        Li("Custom design requirements"),
                        Li("Brand guidelines"),
                        Li("Production applications"),
                        Li("Styling control needed")
                    ),
                    class_="mb-6"
                )
            ),
            
            Section(
                H2("Architecture"),
                
                P("Clear layers:"),
                Ol(
                    Li("CSS variables"),
                    Li("Style classes"),
                    Li("Python tags"),
                    Li("Components")
                ),
                
                P("Benefits:"),
                Ul(
                    Li("Understandable dependencies"),
                    Li("Progressive customization"),
                    Li("Escape hatches available")
                )
            ),
            
            Section(
                H2("Principles"),
                
                Ul(
                    Li("Transparency over magic"),
                    Li("Flexibility over convenience"),
                    Li("Standards over abstractions"),
                    Li("Progressive enhancement")
                )
            ),
            
            Section(
                H2("Contributing"),
                
                P(A("GitHub", href="https://github.com/isaac-flath/EidosUI", target="_blank")),
                P("Contact: isaac@kentro.tech")
            )
        )
    )


@app.get("/demo")
def demo():
    """Live component demo page"""
    return layout(
        "Component Demo",
        create_nav(),
        Div(
            H1("Component Showcase"),
            
            Section(
                H2("Buttons"),
                Div(
                    Button("Default"),
                    Button("Primary", class_=styles.buttons.primary),
                    Button("Secondary", class_=styles.buttons.secondary),
                    Button("Success", class_=styles.buttons.success),
                    Button("Error", class_=styles.buttons.error),
                    Button("Ghost", class_=styles.buttons.ghost),
                    Button("Outline", class_=styles.buttons.outline),
                    class_="flex flex-wrap gap-4 mb-8"
                )
            ),
            
            Section(
                H2("Typography"),
                H1("Heading 1"),
                H2("Heading 2"),
                H3("Heading 3"),
                P(
                    "This is a paragraph with ", Strong("strong text"), ", ",
                    Em("emphasized text"), ", and ", Mark("highlighted text"), "."
                ),
                Blockquote(
                    "This is a blockquote. It stands out from regular text.",
                    Cite("— Citation")
                )
            ),
            
            Section(
                H2("Code Examples"),
                P("Inline code: ", Code("const x = 42")),
                Pre("""def greet(name):
    return f"Hello, {name}!"
    
print(greet("EidosUI"))""")
            ),
            
            Section(
                H2("Forms"),
                Form(
                    Div(
                        Label("Name", for_="name"),
                        Input(type="text", id="name", placeholder="Enter your name"),
                        class_="mb-4"
                    ),
                    Div(
                        Label("Email", for_="email"),
                        Input(type="email", id="email", placeholder="email@example.com"),
                        class_="mb-4"
                    ),
                    Div(
                        Label("Message", for_="message"),
                        Textarea(id="message", placeholder="Your message...", rows=4),
                        class_="mb-4"
                    ),
                    Button("Submit", type="submit", class_=styles.buttons.primary),
                    class_="max-w-md"
                )
            )
        )
    )


if __name__ == "__main__":
    import uvicorn
    print("Starting EidosUI Documentation at http://localhost:8000")
    print("Press Ctrl+C to stop")
    uvicorn.run(app, host="0.0.0.0", port=8000)