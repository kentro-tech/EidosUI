"""EidosUI MVP Showcase - Semantic Typography & Beautiful Buttons"""

import air
import eidos

app = air.Air()

from fastapi.staticfiles import StaticFiles
import os

# Mount static files for CSS
app.mount("/eidos", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "eidos")), name="eidos")

def layout(*content):
    return air.Html(
        air.Head(
            air.Meta(charset="UTF-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            air.Title("EidosUI MVP - Semantic Components"),
            air.Script(src="https://cdn.tailwindcss.com"),
            air.Link(rel="stylesheet", href="/eidos/css/styles.css"),
            air.Link(rel="stylesheet", href="/eidos/css/themes/eidos-variables.css"),
            air.Link(rel="stylesheet", href="/eidos/css/themes/light.css"),
            air.Link(rel="stylesheet", href="/eidos/css/themes/dark.css")
            ),
        eidos.tags.Body(
            air.Main(
                    air.Button("🌙", id="theme-toggle", cls="fixed top-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-800"),
                    *content,
                    cls='p-12'
            ),
            air.RawHTML("""
            <script>
                const toggle = document.getElementById('theme-toggle');
                toggle.addEventListener('click', () => {
                    const html = document.documentElement;
                    const currentTheme = html.getAttribute('data-theme');
                    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                    html.setAttribute('data-theme', newTheme);
                    toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
                });
            </script>
            """)
                )
        )

def Divider():
    return air.Hr(cls='border-4 my-4')

@app.get("/")
def home():
    return layout(
         eidos.tags.H1("EidosUI MVP 🎨"),
         air.P("Beautiful, semantic HTML components with ", air.Em("intelligent"), " theming"),

        Divider(),
        air.Div(
            eidos.tags.H1("H1"),
            eidos.tags.H2("H2"),
            eidos.tags.H3("H3"),
            eidos.tags.H4("H4"),
            eidos.tags.H5("H5"),
            eidos.tags.H6("H6"),
        ),
        Divider(),
        air.Div(
            eidos.tags.Button("Default"),
            eidos.tags.Button("Primary", cls=eidos.styles.buttons.primary),
            eidos.tags.Button("Secondary", cls=eidos.styles.buttons.secondary),
            eidos.tags.Button("Ghost", cls=eidos.styles.buttons.ghost),
            eidos.tags.Button("Outline", cls=eidos.styles.buttons.outline),
            eidos.tags.Button("Success", cls=eidos.styles.buttons.success),
            eidos.tags.Button("Error", cls=eidos.styles.buttons.error),
            eidos.tags.Button("CTA", cls=eidos.styles.buttons.cta),
            cls='space-x-4'
    ),
        
        Divider(),
        
        # Semantic Typography Section
        eidos.tags.H2("Semantic Typography"),
        
        air.P(
            "EidosUI provides ",
            eidos.tags.Strong("strong emphasis"),
            " for important text, ",
            eidos.tags.I("italic styling"),
            " for emphasis, and ",
            eidos.tags.Small("small text"),
            " for fine print. You can also use ",
            eidos.tags.Mark("highlighted text"),
            " to draw attention to specific words."
        ),
        
        air.P(
            "When working with technical content, you might reference ",
            eidos.tags.Var("variables"),
            " or show ",
            eidos.tags.Code("inline code"),
            ". For keyboard shortcuts, use ",
            eidos.tags.Kbd("Ctrl"),
            " + ",
            eidos.tags.Kbd("C"),
            " styling. Sample output looks like ",
            eidos.tags.Samp("Hello, World!"),
            "."
        ),
        
        eidos.tags.Blockquote(
            "Design is not just what it looks like and feels like. Design is how it works.",
            eidos.tags.Cite("— Steve Jobs")
        ),
        
        air.P(
            "Sometimes you need to show ",
            eidos.tags.Del("deleted text"),
            " or use abbreviations like ",
            eidos.tags.Abbr("HTML", title="HyperText Markup Language"),
            ". Meeting scheduled for ",
            eidos.tags.Time("2024-01-15", datetime="2024-01-15"),
            "."
        ),
        
        eidos.tags.Details(
            eidos.tags.Summary("Click to expand more examples"),
            air.Div(
                eidos.tags.H3("Code Examples"),
                eidos.tags.Pre(
                    "def hello_world():\n    print('Hello from EidosUI!')\n    return True"
                ),
                
                eidos.tags.H3("Definition List"),
                eidos.tags.Dl(
                    eidos.tags.Dt("EidosUI"),
                    eidos.tags.Dd("A beautiful, themeable UI component library"),
                    eidos.tags.Dt("Semantic HTML"),
                    eidos.tags.Dd("HTML elements that clearly describe their meaning"),
                    eidos.tags.Dt("CSS Variables"),
                    eidos.tags.Dd("Dynamic styling system for easy theming")
                ),
                
                eidos.tags.H3("Contact Information"),
                eidos.tags.Address(
                    "EidosUI Project",
                    air.Br(),
                    "123 Component Street",
                    air.Br(),
                    "Framework City, UI 12345"
                ),
                cls=eidos.styles.semantic.details_content
            )
        ),
        
        eidos.tags.Figure(
            air.Div(
                "🎨", 
                cls="text-6xl"
            ),
            eidos.tags.Figcaption("The EidosUI logo represents beauty and flexibility")
        ),
        
        eidos.tags.Hr(),
        
        air.P(
            "All semantic elements are styled using CSS variables from ",
            eidos.tags.Code("eidos-variables.css"),
            ", ensuring consistent theming across light and dark modes."
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_example:app", host="0.0.0.0", port=8000, reload=True)