# Getting Started

## Installation

```bash
pip install eidosui
```

With markdown support:
```bash
pip install "eidosui[markdown]"
```

## First App

Create `app.py`:

```python
import air
from air.tags import *
from eidos.tags import *
from eidos.components.headers import EidosHeaders
from eidos.utils import get_eidos_static_directory
from fastapi.staticfiles import StaticFiles

# Create your app
app = air.Air()

# Mount static files for CSS
app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")

@app.get("/")
def home():
    return Html(
        Head(
            *EidosHeaders(),  # Includes all necessary CSS and JS
            Title("My First EidosUI App")
        ),
        Body(
            Main(
                H1("Welcome to EidosUI!"),
                P("This is your first EidosUI application."),
                Button("Click Me", class_="eidos-button-primary"),
                class_="p-12"
            )
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Run

```bash
python app.py
```

Visit `http://localhost:8000`

## Basic Usage

### Styled HTML Tags

```python
from eidos.tags import *

# Typography
H1("Large Heading")
H2("Section Heading")
P("A paragraph with ", Strong("strong"), " and ", Em("emphasized"), " text.")
Small("Fine print")
Mark("Highlighted text")

# Interactive Elements
Button("Primary Action", class_=styles.buttons.primary)
Button("Secondary", class_=styles.buttons.secondary)

# Code and Technical
Code("inline_code()")
Pre("def hello():\n    print('Hello, World!')")
Kbd("Ctrl"), " + ", Kbd("C")
```

### Style System

```python
import eidos.styles as styles

# Button styles
Button("Primary", class_=styles.buttons.primary)
Button("Secondary", class_=styles.buttons.secondary)
Button("Success", class_=styles.buttons.success)
Button("Error", class_=styles.buttons.error)

# Typography styles
H1("Heading", class_=styles.typography.h1)
P("Text", class_=styles.typography.body)
```

### Themes

```python
# Add theme toggle button
Button(
    "🌙",
    class_="theme-toggle p-2 rounded-full",
    onclick="toggleTheme()"
)

# Include theme toggle script
Script("""
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
}
""")
```

## Project Structure

```
my-app/
├── app.py              # Main application file
├── components/         # Custom components
│   └── layout.py
├── static/            # Additional static assets
│   └── custom.css
└── templates/         # Page templates
    ├── home.py
    └── about.py
```

## Components

### Navigation

```python
from eidos.components.navigation import NavBar

NavBar(
    A("Home", href="/"),
    A("About", href="/about"),
    A("Contact", href="/contact"),
    lcontents=H3("My App"),  # Left content
    sticky=True,             # Stick to top on scroll
    scrollspy=True          # Highlight active section
)
```

### Layout

```python
def layout(title, *content):
    return Html(
        Head(
            *EidosHeaders(),
            Title(title)
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("About", href="/about"),
                lcontents=H3("My App")
            ),
            Main(
                *content,
                class_="p-12"
            )
        )
    )

# Use in routes
@app.get("/")
def home():
    return layout(
        "Home",
        H1("Welcome!"),
        P("This is the home page.")
    )
```

## Static Files

```python
from fastapi.staticfiles import StaticFiles
from eidos.utils import get_eidos_static_directory

# Mount EidosUI static files
app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")

# Mount your own static files
app.mount("/static", StaticFiles(directory="static"), name="static")
```

## Common Patterns

### Forms

```python
Form(
    Label("Name:", for_="name"),
    Input(type="text", id="name", name="name"),
    
    Label("Email:", for_="email"),
    Input(type="email", id="email", name="email"),
    
    Button("Submit", type="submit", class_=styles.buttons.primary),
    
    method="POST",
    action="/submit"
)
```

### Cards

```python
Div(
    H3("Card Title"),
    P("Card content goes here."),
    Button("Action", class_=styles.buttons.outline),
    class_="p-6 rounded-lg shadow-lg"
)
```

### Responsive Grid

```python
Div(
    *[Card(f"Item {i}") for i in range(6)],
    class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"
)