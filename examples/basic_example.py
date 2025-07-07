"""EidosUI MVP Showcase - Semantic Typography & Beautiful Buttons"""

from air import *
from eidos.tags import *
import eidos.styles as styles
from eidos.components.headers import EidosHeaders
from eidos.utils import get_eidos_static_directory

app = air.Air()

from fastapi.staticfiles import StaticFiles

# Mount static files for CSS
app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")

def layout(*content):
    return Html(
        Head(
            *EidosHeaders(),
            Title("EidosUI MVP 🎨"),
        ),
        Body(
            Main(
                Button("🌙", id="theme-toggle", cls="fixed top-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-800"),
            *content,
            cls='p-12'
        ),
        air.Script("""
            const toggle = document.getElementById('theme-toggle');
            toggle.addEventListener('click', () => {
                const html = document.documentElement;
                const currentTheme = html.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                html.setAttribute('data-theme', newTheme);
                toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
            });
        """),
    ))

def Divider():
    return air.Hr(cls='border-4 my-4')

@app.get("/")
def home():
    return layout(
         H1("EidosUI MVP 🎨"),
         P("Beautiful, semantic HTML components with ", Em("intelligent"), " theming"),

        Divider(),
        air.Div(
            H1("H1"),
            H2("H2"),
            H3("H3"),
            H4("H4"),
            H5("H5"),
            H6("H6"),
        ),
        Divider(),
        air.Div(
            Button("Default"),
            Button("Primary", cls=styles.buttons.primary),
            Button("Secondary", cls=styles.buttons.secondary),
            Button("Ghost", cls=styles.buttons.ghost),
            Button("Outline", cls=styles.buttons.outline),
            Button("Success", cls=styles.buttons.success),
            Button("Error", cls=styles.buttons.error),
            Button("CTA", cls=styles.buttons.cta),
            cls='space-x-4'
    ),
        
        Divider(),
        
        # Semantic Typography Section
        H2("Semantic Typography"),
        
        air.P(
            "EidosUI provides ",
            Strong("strong emphasis"),
            " for important text, ",
            I("italic styling"),
            " for emphasis, and ",
            Small("small text"),
            " for fine print. You can also use ",
            Mark("highlighted text"),
            " to draw attention to specific words."
        ),
        
        air.P(
            "When working with technical content, you might reference ",
            Var("variables"),
            " or show ",
            Code("inline code"),
            ". For keyboard shortcuts, use ",
            Kbd("Ctrl"),
            " + ",
            Kbd("C"),
            " styling. Sample output looks like ",
            Samp("Hello, World!"),
            "."
        ),
        
        Blockquote(
            "Design is not just what it looks like and feels like. Design is how it works.",
            Cite("— Steve Jobs")
        ),
        
        air.P(
            "Sometimes you need to show ",
            Del("deleted text"),
            " or use abbreviations like ",
            Abbr("HTML", title="HyperText Markup Language"),
            ". Meeting scheduled for ",
            Time("2024-01-15", datetime="2024-01-15"),
            "."
        ),
        
        Details(
            Summary("Click to expand more examples"),
            air.Div(
                H3("Code Examples"),
                Pre(
                    "def hello_world():\n    print('Hello from EidosUI!')\n    return True"
                ),
                
                H3("Definition List"),
                Dl(
                    Dt("EidosUI"),
                    Dd("A beautiful, themeable UI component library"),
                    Dt("Semantic HTML"),
                    Dd("HTML elements that clearly describe their meaning"),
                    Dt("CSS Variables"),
                    Dd("Dynamic styling system for easy theming")
                ),
                
                H3("Contact Information"),
                Address(
                    "EidosUI Project",
                    air.Br(),
                    "123 Component Street",
                    air.Br(),
                    "Framework City, UI 12345"
                ),
                cls=styles.semantic.details_content
            )
        ),
        
        Figure(
            Div(
                "🎨", 
                cls="text-6xl"
            ),
            Figcaption("The EidosUI logo represents beauty and flexibility")
        ),
        
        Hr(),
        
        air.P(
            "All semantic elements are styled using CSS variables from ",
            Code("eidos-variables.css"),
            ", ensuring consistent theming across light and dark modes."
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_example:app", host="0.0.0.0", port=8000, reload=True)