"""EidosUI MVP Showcase - Semantic Typography & Beautiful Buttons"""

import fastapi_tags as ft
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os


# Import EidosUI MVP - semantic HTML + forms!
from eidos import (
    H1, H2, H3, P, Text, Em, Strong, A, Code, Pre, Mark, Small, Button,
    serve_eidos_static, create_eidos_head_components,
    button_styles, typography_styles
)

app = FastAPI()

# Mount only light theme, no dark theme
serve_eidos_static(app)

# Serve custom themes from examples directory
app.mount("/static", StaticFiles(directory='static'))

def page_header():
    return ft.Header(
        H1("EidosUI MVP 🎨"),
        P("Beautiful, semantic HTML components with ", Em("intelligent"), " theming"),
        cls="text-center mb-12"
    )

def typography_section():
    return ft.Section(
        H2("Semantic Typography"),
        P("Use proper HTML semantics with beautiful styling:"),
        ft.Div(
            P("This is a ", Strong("paragraph"), " with ", Em("emphasis"), " and a ", 
              A("styled link", href="#"), "."),
            P("Code example: ", Code("button_styles.primary")),
            P("Highlighted text: ", Mark("important notice")),
            P(Small("Small print and legal text")),
            Pre("""def example():
    print("Preformatted code block")
    return True"""),
            cls="space-y-4 mb-8"
        ),
        cls="mb-12"
    )

def button_system_section():
    return ft.Section(
        H2("Beautiful Button System"),
        P("Color-coded for perfect UX with smooth interactions:"),
        
        ft.Div(
            H3("Semantic Actions", cls="text-lg font-semibold mb-3"),
            ft.Div(
                Button("Primary Action"),
                Button("Secondary", cls=button_styles.secondary),
                Button("Call to Action", cls=button_styles.cta),
                cls="flex flex-wrap gap-3 mb-6"
            ),
            
            H3("Status Actions", cls="text-lg font-semibold mb-3"),
            ft.Div(
                Button("Success", cls=button_styles.success),
                Button("Warning", cls=button_styles.warning),
                Button("Error", cls=button_styles.error),
                cls="flex flex-wrap gap-3 mb-6"
            ),
            
            H3("Alternative Styles", cls="text-lg font-semibold mb-3"),
            ft.Div(
                Button("Ghost Button", cls=button_styles.ghost),
                Button("Outlined", cls=button_styles.outline_primary),
                Button("Link Style", cls=button_styles.link),
                cls="flex flex-wrap gap-3"
            ),
            cls="space-y-2"
        ),
        cls="mb-12"
    )

def accessibility_section():
    return ft.Section(
        H2("Responsive & Accessible"),
        P("Built with modern UX patterns:"),
        ft.Ul(
            ft.Li("Focus rings for keyboard navigation"),
            ft.Li("Hover states with smooth transitions"),
            ft.Li("Active states with subtle scale feedback"),
            ft.Li("High contrast colors that adapt to theme"),
            ft.Li("Semantic HTML for screen readers"),
            cls="list-disc list-inside space-y-2 text-text-muted"
        ),
        cls="mb-12"
    )

def theme_setup():
    return ft.Script("""
        // Register custom themes from examples folder
        registerTheme('win80s', '/static/win80s.css');
        registerTheme('artist', '/static/artist.css');
        registerTheme('chaos', '/static/chaos.css');
    """)

def theme_switcher():
    return ft.Button(
        "Change Theme",
        onclick="toggleTheme()",
        cls="fixed top-6 right-6 p-3 rounded-lg bg-[var(--color-surface)] hover:bg-[var(--color-surface-elevated)] border border-[var(--color-border)] shadow-lg transition-all duration-200 hover:shadow-xl",
        title="Toggle theme"
    )

def page():
    return ft.Html(
        ft.Head(
            ft.Meta(charset="UTF-8"),
            ft.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            ft.Title("EidosUI MVP - Semantic Components"),
            ft.Script(src="https://cdn.tailwindcss.com"),
            *create_eidos_head_components(themes=["light"])
        ),
        ft.Body(
            ft.Div(
                page_header(),
                typography_section(),
                button_system_section(),
                accessibility_section(),
                cls="max-w-4xl mx-auto px-6 py-12 space-y-8"
            ),
            theme_setup(),
            theme_switcher(),
            cls="min-h-screen bg-[var(--color-background)] text-[var(--color-text)]"
        )
    )

@app.get("/", response_class=ft.FTResponse)
def home():
    return page()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_example:app", host="0.0.0.0", port=8000, reload=True)