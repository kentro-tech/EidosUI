"""EidosUI MVP Showcase - Semantic Typography & Beautiful Buttons"""

import fastapi_tags as ft
from fastapi import FastAPI

# Import EidosUI MVP - semantic HTML + forms!
from eidos import (
    H1, H2, H3, P, Text, Em, Strong, A, Button,
    serve_eidos_static, create_eidos_head_tag,
    button_styles, typography_styles
)

app = FastAPI()

# 🎉 One line setup - no manual file mounting!
serve_eidos_static(app)


@app.get("/", response_class=ft.FTResponse)
def home():
    """EidosUI MVP showcase"""
    
    
    # Simple page content using semantic HTML
    page_content = ft.Div(
        ft.Header(
            H1("EidosUI MVP 🎨"),
            P("Beautiful, semantic HTML components with ", Em("intelligent"), " theming"),
            cls="text-center mb-12"
        ),
        
        ft.Section(
            H2("Semantic Typography"),
            P("Use proper HTML semantics with beautiful styling:"),
            ft.Div(
                P("This is a ", Strong("paragraph"), " with ", Em("emphasis"), " and a ", 
                  A("styled link", href="#"), "."),
                P("Code example: ", ft.Code("button_styles.primary")),
                # ft.Blockquote("\"Great design is invisible.\" - Good design is obvious."),
                cls="space-y-4 mb-8"
            ),
            cls="mb-12"
        ),
        
        ft.Section(
            H2("Beautiful Button System"),
            P("Color-coded for perfect UX with smooth interactions:"),
            
            ft.Div(
                H3("Semantic Actions", cls="text-lg font-semibold mb-3"),
                ft.Div(
                    Button("Primary Action", cls=button_styles.primary, size_cls=button_styles.md),
                    Button("Secondary", cls=button_styles.secondary, size_cls=button_styles.md),
                    Button("Call to Action", cls=button_styles.cta, size_cls=button_styles.md),
                    cls="flex flex-wrap gap-3 mb-6"
                ),
                
                H3("Status Actions", cls="text-lg font-semibold mb-3"),
                ft.Div(
                    Button("Success", cls=button_styles.success, size_cls=button_styles.md),
                    Button("Warning", cls=button_styles.warning, size_cls=button_styles.md),
                    Button("Error", cls=button_styles.error, size_cls=button_styles.md),
                    cls="flex flex-wrap gap-3 mb-6"
                ),
                
                H3("Alternative Styles", cls="text-lg font-semibold mb-3"),
                ft.Div(
                    Button("Ghost Button", cls=button_styles.ghost, size_cls=button_styles.md),
                    Button("Outlined", cls=button_styles.outline_primary, size_cls=button_styles.md),
                    Button("Link Style", cls=button_styles.link, size_cls=button_styles.md),
                    cls="flex flex-wrap gap-3"
                ),
                cls="space-y-2"
            ),
            cls="mb-12"
        ),
        
        ft.Section(
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
        ),
        
        cls="max-w-4xl mx-auto px-6 py-12 space-y-8"
    )
    
    # Return complete HTML page
    return ft.Html(
        create_eidos_head_tag(title="EidosUI MVP - Semantic Components"),
        ft.Body(
            page_content,
            # Theme switcher
            ft.Button(
                "🌙",
                onclick="toggleTheme()",
                cls="fixed top-6 right-6 p-3 rounded-lg bg-[var(--color-surface)] hover:bg-[var(--color-surface-elevated)] border border-[var(--color-border)] shadow-lg transition-all duration-200 hover:shadow-xl",
                title="Toggle theme"
            ),
            cls="min-h-screen bg-[var(--color-background)] text-[var(--color-text)]"
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("basic_example:app", host="0.0.0.0", port=8000, reload=True)