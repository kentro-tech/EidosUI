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
```

## Run

```bash
fastapi dev
```

Visit `http://localhost:8000`

## Basic Usage

### Styled HTML Tags

```python
from eidos.tags import *

H1("Large Heading")
H2("Section Heading")
P("A paragraph with ", Strong("strong"), " and ", Em("emphasized"), " text.")
Button("Primary Action")
Code("inline_code()")
```

### Style System

```python
import eidos.styles as styles

# Button styles
Button("Primary", class_=styles.buttons.cta)
Button("Secondary", class_=styles.buttons.secondary)
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
