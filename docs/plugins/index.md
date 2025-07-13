# EidosUI Plugins

EidosUI's plugin system allows you to extend functionality while maintaining consistency with the core library.

## Available Plugins

- [markdown](/plugins/markdown): Markdown rendering with EidosUI styling.

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
