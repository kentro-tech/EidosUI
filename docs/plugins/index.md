# EidosUI Plugins

EidosUI's plugin system allows you to extend functionality while maintaining consistency with the core library.

## Available Plugins

### Markdown Plugin

The official Markdown plugin provides rich markdown rendering with EidosUI styling.

**Installation:**
```bash
pip install "eidosui[markdown]"
```

**Features:**
- GitHub Flavored Markdown support
- Syntax highlighting for code blocks
- GitHub-style alerts ([!NOTE], [!WARNING], etc.)
- Table of contents generation
- Theme-aware styling
- Custom extension support

**Usage:**
```python
from eidos.plugins.markdown import Markdown, MarkdownCSS

# In your HTML head
Head(
    *EidosHeaders(),
    MarkdownCSS()  # Include markdown styles
)

# Render markdown content
content = Markdown("""
# Hello World

This is **bold** and this is *italic*.

> [!NOTE]
> This is a GitHub-style alert.

```python
def hello():
    return "Hello, EidosUI!"
```
""")
```

[Learn more about the Markdown plugin →](markdown.md)

## Plugin Architecture

### How Plugins Work

Plugins in EidosUI:
1. Extend core functionality without modifying it
2. Use CSS variables for consistent theming
3. Provide Python components and/or CSS styles
4. Can include optional JavaScript for interactivity

### Plugin Structure

```
my_plugin/
├── __init__.py          # Main exports
├── components.py        # Python components
├── styles.css          # Plugin styles
├── static/             # Static assets
│   └── plugin.js       # Optional JavaScript
└── extensions/         # Optional extensions
    └── custom.py
```

## Creating a Plugin

### 1. Basic Plugin

```python
# my_plugin/__init__.py
from air.tags import Div, Style

def PluginComponent(content, **kwargs):
    """A custom plugin component"""
    return Div(
        Style("""
            .my-plugin-component {
                padding: var(--eidos-spacing-4);
                background: var(--eidos-bg-secondary);
                border-radius: var(--eidos-border-radius);
            }
        """),
        Div(
            content,
            class_="my-plugin-component",
            **kwargs
        )
    )

# CSS helper
def PluginCSS():
    """Include plugin styles"""
    return Link(
        rel="stylesheet",
        href="/static/my_plugin/styles.css"
    )
```

### 2. Theme-Aware Plugin

```css
/* my_plugin/styles.css */
.my-plugin-component {
    /* Use EidosUI variables */
    color: var(--eidos-text-primary);
    background: var(--eidos-bg-secondary);
    border: 1px solid var(--eidos-border-color);
}

/* Support dark mode */
[data-theme="dark"] .my-plugin-component {
    background: var(--eidos-gray-800);
}
```

### 3. Interactive Plugin

```python
# Components with behavior
def Carousel(items, **kwargs):
    return Div(
        Div(
            *[Div(item, class_="carousel-item") for item in items],
            class_="carousel-container"
        ),
        Script(src="/static/my_plugin/carousel.js"),
        class_="eidos-carousel",
        **kwargs
    )
```

## Plugin Best Practices

### 1. Use CSS Variables

Always use EidosUI's CSS variables:

```css
/* Good */
.plugin-alert {
    color: var(--eidos-info-text);
    background: var(--eidos-info-bg);
}

/* Avoid */
.plugin-alert {
    color: #0366d6;
    background: #f0f8ff;
}
```

### 2. Namespace Your Classes

Prefix CSS classes to avoid conflicts:

```css
.my-plugin-card { }
.my-plugin-header { }
```

### 3. Progressive Enhancement

Ensure basic functionality without JavaScript:

```python
def Tabs(tabs):
    # Works with CSS :target
    return Div(
        # Tab buttons
        Div(*[
            A(tab.title, href=f"#{tab.id}")
            for tab in tabs
        ]),
        # Tab content
        *[Div(
            tab.content,
            id=tab.id,
            class_="tab-pane"
        ) for tab in tabs]
    )
```

### 4. Provide Helpers

Include CSS/JS loading helpers:

```python
def MyPluginHeaders():
    """Include all plugin assets"""
    return [
        Link(rel="stylesheet", href="/static/my_plugin/styles.css"),
        Script(src="/static/my_plugin/script.js", defer=True)
    ]
```

## Distributing Plugins

### PyPI Package

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="eidosui-my-plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "eidosui>=0.2.0",
    ],
    package_data={
        "my_plugin": ["static/*", "styles.css"],
    },
    description="My plugin for EidosUI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
```

### Documentation

Include clear documentation:

```markdown
# EidosUI My Plugin

## Installation

```bash
pip install eidosui-my-plugin
```

## Usage

```python
from my_plugin import PluginComponent, PluginCSS

# Include CSS
Head(*EidosHeaders(), PluginCSS())

# Use component
PluginComponent("Hello from plugin!")
```
```

## Plugin Ideas

### Data Visualization
- Charts and graphs using CSS variables
- Data tables with sorting/filtering
- Progress indicators

### Form Enhancements
- Advanced form controls
- Validation helpers
- Multi-step forms

### Layout Components
- Advanced grids
- Masonry layouts
- Sidebar systems

### Media Components
- Image galleries
- Video players
- Audio controls

### Interactive Elements
- Tooltips and popovers
- Date/time pickers
- Autocomplete inputs

## Testing Plugins

```python
def test_plugin_component():
    """Test plugin renders correctly"""
    result = PluginComponent("Test content")
    assert "my-plugin-component" in str(result)
    assert "Test content" in str(result)

def test_plugin_theming():
    """Test plugin uses CSS variables"""
    css = open("my_plugin/styles.css").read()
    assert "var(--eidos-" in css
```

## Contributing Plugins

We welcome plugin contributions! Guidelines:

1. Follow EidosUI design principles
2. Use CSS variables for theming
3. Include comprehensive documentation
4. Add tests for your components
5. Ensure accessibility
6. Submit a PR to the [awesome-eidosui](https://github.com/isaac-flath/awesome-eidosui) list

## Resources

- [Plugin Development Guide](plugin-development.md)
- [Markdown Plugin Source](https://github.com/isaac-flath/EidosUI/tree/main/eidos/plugins/markdown)
- [CSS Variable Reference](../styling.md#css-variable-system)
- [Component Patterns](../components.md#component-patterns)