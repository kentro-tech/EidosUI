# EidosUI

Python UI components with CSS variables for theming.

## Features

- Python components
- CSS variable theming
- Semantic HTML
- Tailwind CSS compatible
- Plugin system

## Documentation

- [Getting Started](getting-started.md) - Installation and first app
- [Components](components.md) - All available components
- [Styling](styling.md) - Themes and customization
- [Philosophy](philosophy.md) - Design decisions
- [Plugins](plugins/index.md) - Extensions and markdown support

## Quick Example

```python
import air
from eidos.tags import *
from eidos.components.navigation import NavBar
import eidos.styles as styles

app = air.Air()

@app.get("/")
def home():
    return Html(
        Head(
            *EidosHeaders(),
            Title("My EidosUI App")
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("About", href="/about"),
                lcontents=H3("My App"),
                sticky=True
            ),
            Main(
                H1("Welcome to EidosUI"),
                P("Build beautiful UIs with semantic HTML and modern styling."),
                Button("Get Started", class_=styles.buttons.primary),
                class_="p-12"
            )
        )
    )
```

## Core Concepts

### 1. Semantic HTML First
EidosUI wraps standard HTML elements with intelligent defaults while preserving their semantic meaning.

### 2. CSS Variables for Theming
All styling uses CSS variables, making themes easy to create and switch between.

### 3. Python-Native API
Components are Python functions and classes, providing type hints and IDE support.

### 4. Progressive Enhancement
Start with basic HTML and progressively add styling and interactivity as needed.

## Next Steps

- [Install EidosUI](getting-started.md#installation) and create your first app
- Explore the [component library](components.md) to see what's available
- Learn about [creating custom themes](styling.md#custom-themes)
- Check out the [example applications](https://github.com/isaac-flath/EidosUI/tree/main/examples)