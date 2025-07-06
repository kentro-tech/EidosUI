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
                    *content
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
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_example:app", host="0.0.0.0", port=8000, reload=True)