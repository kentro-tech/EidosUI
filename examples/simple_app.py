"""
The simplest possible EidosUI application.

This example shows the minimal code needed to create a web page with EidosUI.
"""

import air
from eidos import *

# Create the Air application
app = air.Air()

@app.get("/")
def home():
    """Simple homepage with EidosUI components."""
    return Html(
        Head(
            Title("Welcome to EidosUI"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Welcome to EidosUI"),
                P("This is the simplest possible EidosUI application."),
                P(
                    Code("EidosUI"), " provides ", Strong("beautiful"), " styled components that work ", I("out of the box.")
                ),
                Button("Click me!", onclick="alert('Hello from EidosUI!')"),
                class_="container mx-auto p-8 space-y-4"
            ),
        ),
    )