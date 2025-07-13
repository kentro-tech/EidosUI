# Quick Start

## Installation

```bash
pip install eidosui
```

## First App

Create `app.py`:

```python
from eidos import *
import air

app = air.Air()

@app.get("/")
def home():
    return Html(
        Head(
            Title("My App"),
            *EidosHeaders()
        ),
        Body(
            H1("Welcome to EidosUI"),
            P(
                Code("EidosUI"), " provides ", Strong("beautiful"), " styled components that work ", I("out of the box.")
            ),
            Button("A Button"),
            DataTable.from_lists(
                [["Alice", "30"], ["Bob", "25"]], 
                headers=["Name", "Age"]
            ),
            class_='space-y-5'
        )
    )
```

Run:
```bash
fastapi dev app.py
```
## Core Concepts

### Styled Tags

These are Styled versions of Tags that are available in the base `air` library.

```python
H1("Title")
P("Text with ", Strong("bold"), " and ", Em("italic"))
Button("Click me")
Code("print('hello')")
```

### Components

Components built on top of styled tags to create new components, which are generally more complex than Tags.  Ultimately, they still return an `AirTag` they're just a more complicated.

```python
# Tables
DataTable.from_lists(data, headers=["Col1", "Col2"])
DataTable.from_dicts([{"name": "Alice", "age": 30}])

# Navigation
NavBar(
    A("Home", href="/"),
    A("About", href="/about"),
    lcontents=H3("My App")
)
```

### Themes

```python
Html(data_theme="dark")  # or "light"
```

### Custom Styling

```python
H1("Red Title", class_="text-red-500")
Button("Large", class_="text-lg px-8 py-4")
```

## Next Steps

- [Concepts](concepts) - Understand the architecture
- [Kitchen Sink](kitchen-sink) - See all components
- [API Reference](api) - Detailed documentation