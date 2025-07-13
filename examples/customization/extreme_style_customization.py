"""
Example of using EidosUI with a custom theme.

This shows how to override the default CSS variables to create your own theme.
"""

import air
from eidos import *

app = air.Air()

with open("custom_theme.css", "r") as f:
    CUSTOM_THEME = f.read()

@app.get("/")
def home():
    """Homepage with custom theme."""
    return Html(
        Head(
            *EidosHeaders(),  # Include EidosUI's default styles
            Style(CUSTOM_THEME),  # Apply our custom theme
            # Include artsy fonts
            air.Link(
                href="https://fonts.googleapis.com/css2?family=Bungee&family=Space+Mono:wght@400;700&display=swap",
                rel="stylesheet"
            ),
        ),
        Body(
            Div(
                H1("ABSTRACT ART THEME"),
                P("Welcome to the ", Strong("WILDEST"), " theme you've ever seen!"),

                H2("MONDRIAN MEETS MEMPHIS", class_="mt-8"),
                P(
                    "This theme takes inspiration from ", Code("abstract art movements"), " like ",
                    I("De Stijl"), " and ", I("Memphis Design"), " to create something ",
                    Strong("TOTALLY UNIQUE!")
                ),

                Div(
                    Button("HOT PINK!"),
                    Button("BOLD YELLOW!", class_=buttons.secondary),
                    Button("GHOST MODE!", class_=buttons.ghost),
                    class_="space-x-4 mt-4"
                ),

                H3("Features of this ARTSY theme:", class_="mt-8"),
                Ul(
                    Li("🎨 Hot pink & yellow color scheme"),
                    Li("📐 Geometric patterns everywhere"),
                    Li("🔤 Bungee display font for headings"),
                    Li("🎯 Sharp corners (no border radius)"),
                    Li("💫 Elements with slight rotation"),
                    Li("🎪 Memphis-style decorations"),
                    Li("〰️ Squiggly underlines"),
                    Li("🔶 Random shapes after paragraphs"),
                    class_="space-y-2 list-none"
                ),

                P(
                    "Every element has been ", Strong("TRANSFORMED"), " to show that EidosUI ",
                    "can be styled to match ", I("ANY"), " design vision - even the most ",
                    Mark("AVANT-GARDE"), " ones!",
                    class_="mt-6 text-lg"
                ),

                class_="container mx-auto p-8 space-y-4"
            )
        )
    )