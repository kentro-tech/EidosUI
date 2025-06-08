# EidosUI 🎨

A modern, flexible Tailwind CSS-based UI library for Python web frameworks. Built for maximum developer flexibility while providing excellent defaults.

## ✨ Key Features

- **🎨 CSS Variable Theming**: Light/dark themes with easy customization
- **📱 Mobile-First Responsive**: All components designed mobile-first
- **🔧 Maximum Flexibility**: Use our styles, custom Tailwind classes, or mix both
- **⚡ FastAPI-Tags Integration**: Built specifically for modern Python web development
- **🎯 Zero Lock-in**: Components expose CSS classes directly - no hidden magic

## 🚀 Quick Start

### Installation with UV (Recommended)

```bash
# Create a new project with UV
uv init my-eidos-app
cd my-eidos-app

# Add EidosUI as a dependency
uv add eidos-ui

# For development, add optional dependencies
uv add eidos-ui[examples] --dev
```

### Installation with pip

```bash
pip install eidos-ui

# For development with examples
pip install eidos-ui[examples]
```

### Development Setup with UV

To contribute or run examples:

```bash
# Clone the repository
git clone https://github.com/isaac-flath/EidosUI.git
cd EidosUI

# Install in editable mode with all dependencies
uv sync --all-extras

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run examples
cd examples
python basic_example.py

# Or run directly with uv
uv run python examples/basic_example.py
```

## 🔧 UV Best Practices

EidosUI is optimized for UV, the fast Python package installer and resolver:

### For End Users

```bash
# Add to your project
uv add eidos-ui

# With optional dependencies for examples/development
uv add eidos-ui[examples,dev]

# Run your app
uv run python your_app.py
```

### For Contributors

```bash
# One-time setup
git clone https://github.com/isaac-flath/EidosUI.git
cd EidosUI
uv sync --all-extras

# Daily development
source .venv/bin/activate  # Or use uv run for individual commands
python examples/basic_example.py

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .
```

### Python Version Support

EidosUI supports Python 3.9+ and is tested on:
- Python 3.9, 3.10, 3.11, 3.12
- Compatible with both pip and UV
- Optimized for UV's speed and reliability
```

### Basic Usage

```python
from fastapi import FastAPI
import fastapi_tags as ft
from eidos import H1, Button, Container, serve_eidos_static, create_eidos_head_tag

app = FastAPI()

# 🎉 One line to serve all EidosUI static files!
serve_eidos_static(app)

@app.get("/")
def home():
    page = Container(
        H1("Hello, EidosUI!"),
        Button("Click me", cls="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"),
        Button("Styled Button", cls=button_styles.primary)
    )
    
    # Easy HTML head creation with fastapi-tags
    return ft.Html(
        create_eidos_head_tag(title="My App"),
        ft.Body(page, cls=layout_styles.page)
    )
```

## 🎨 Theme System

EidosUI uses CSS variables for theming, making it compatible with any theme generator. Multiple setup options:

**Option 1: Auto-serve files (recommended)**
```python
from eidos import serve_eidos_static, create_eidos_head_tag

serve_eidos_static(app)  # One line setup!

# Then use fastapi-tags components:
return ft.Html(
    create_eidos_head_tag(title="My App"),
    ft.Body(content)
)
```

**Option 2: Inline everything (single-file deployments)**
```python
from eidos import create_inline_eidos_head_tag

# All CSS/JS embedded - no external files needed
return ft.Html(
    create_inline_eidos_head_tag(title="My App"),
    ft.Body(content)
)
```

**Option 3: Custom control**
```python
from eidos import get_theme_css, get_eidos_js

# Get raw CSS/JS content for processing
css = get_theme_css("light")
js = get_eidos_js()
```

### Theme Switching

```python
# Add a theme switcher button
theme_button = ft.Button(
    ft.Span("☀️", cls="block [data-theme='dark']:hidden"),
    ft.Span("🌙", cls="hidden [data-theme='dark']:block"),
    onclick="toggleTheme()",
    cls="p-2 rounded-lg bg-surface hover:bg-surface-elevated"
)
```

## 📖 Component Philosophy

EidosUI components are **class-based and flexible**:

### ✅ Three Ways to Style

1. **Use provided dataclass styles** (good defaults):
```python
Button("Save", cls=button_styles.primary, size_cls=button_styles.lg)
```

2. **Use custom Tailwind classes** (full control):
```python
Button("Save", cls="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-lg")
```

3. **Mix both approaches** (best of both worlds):
```python
Card(
    H1("Title"),
    Text("Content"),
    cls=card_styles.elevated,  # Use our styles
    padding_cls="p-8"          # Add custom padding
)
```

## 🧩 Available Components

### Typography
```python
from eidos import H1, H2, H3, H4, H5, H6, Text, Link, Code

H1("Main Heading")  # Mobile-first responsive
Text("Body text", cls=typography_styles.body)
Link("Click here", href="/page")
```

### Layout
```python
from eidos import Container, Card, Grid, Stack, Flex, Center

Container(
    Grid(
        Card("Card 1", cls=card_styles.default),
        Card("Card 2", cls=card_styles.elevated),
        cls=layout_styles.grid_responsive  # Responsive grid
    ),
    size_cls=layout_styles.container_lg
)
```

### Forms
```python
from eidos import Button, Input, Label, FormGroup

FormGroup(
    Label("Email"),
    Input(type="email", placeholder="you@example.com"),
    Button("Submit", cls=button_styles.primary)
)
```

## 📊 Style Dataclasses

Access comprehensive style collections:

```python
from eidos import button_styles, card_styles, form_styles, layout_styles

# Button variations
button_styles.primary      # Main CTA style
button_styles.secondary    # Secondary actions
button_styles.ghost        # Subtle buttons
button_styles.outline_primary  # Outlined style

# Card variations
card_styles.default        # Basic card
card_styles.elevated       # With shadow
card_styles.interactive    # Hover effects

# Layout helpers
layout_styles.container    # Responsive container
layout_styles.grid_responsive  # Auto-responsive grid
layout_styles.flex_center # Center content
```

## 🎯 Examples

### Complete Page Example

```python
from fastapi import FastAPI
from eidos import *

app = FastAPI()

@app.get("/")
def dashboard():
    return Container(
        # Header
        Flex(
            H1("Dashboard", cls=typography_styles.h1),
            Button("Settings", cls=button_styles.ghost),
            cls=layout_styles.flex_between
        ),
        
        # Stats Grid
        Grid(
            Card(
                H3("Users", cls=typography_styles.h3),
                Text("1,234", cls="text-3xl font-bold text-primary"),
                cls=card_styles.default,
                padding_cls=card_styles.comfortable
            ),
            Card(
                H3("Revenue", cls=typography_styles.h3),
                Text("$12,345", cls="text-3xl font-bold text-success"),
                cls=card_styles.default,
                padding_cls=card_styles.comfortable
            ),
            cls=layout_styles.grid_responsive
        ),
        
        # Content Area
        Card(
            H2("Recent Activity"),
            Stack(
                Text("User John signed up"),
                Text("Order #123 completed"),
                Text("Payment received"),
                cls=layout_styles.stack_sm
            ),
            cls=card_styles.elevated,
            padding_cls=card_styles.comfortable
        ),
        
        cls=layout_styles.stack_lg,
        size_cls=layout_styles.container_lg
    )
```

## 🛠 Development

### Local Development with UV

```bash
# Clone the repo
git clone https://github.com/isaac-flath/EidosUI
cd EidosUI

# Install with UV
uv install

# Run example
cd examples
uv run python basic_example.py
```

### Project Structure

```
eidos/
├── core/               # Core theme and style system
│   ├── themes.py      # Theme management
│   ├── styles.py      # Style dataclasses
│   └── utils.py       # Utilities
├── components/         # UI components
│   ├── typography.py  # Text components
│   ├── layout.py      # Layout components
│   └── forms.py       # Form components
├── themes/            # CSS theme files
│   ├── light.css      # Light theme
│   └── dark.css       # Dark theme
└── static/            # JavaScript utilities
    └── eidos-ui.js    # Theme switching
```

## 🤝 Contributing

Contributions welcome! EidosUI follows MVP principles:

- **Simple and focused**: Each component does one thing well
- **Flexible by default**: Always expose `cls` for customization
- **Mobile-first**: Responsive design in everything
- **Minimal dependencies**: Just fastapi-tags + CSS variables

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Credits

Built with [fastapi-tags](https://github.com/fastapi-users/fastapi-tags) and inspired by modern UI libraries while maintaining Python-first DX.