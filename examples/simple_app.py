"""
The simplest possible EidosUI application.

This example shows the minimal code needed to create a web page with EidosUI.
"""

import air
from eidos import *
from eidos.utils import get_eidos_static_files
from fastapi.staticfiles import StaticFiles

# Create the Air application
app = air.Air()

# Mount static files for CSS and JS - only mount specific directories for security
for mount_path, directory in get_eidos_static_files(markdown=True).items():
    app.mount(mount_path, StaticFiles(directory=directory), name=mount_path.strip('/'))


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