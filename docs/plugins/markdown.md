# Markdown Plugin

Theme-aware markdown rendering with GitHub Flavored Markdown support.

## Installation

```bash
pip install "eidosui[markdown]"
```

## Basic Usage

```python
from eidos.plugins.markdown import Markdown, MarkdownCSS, MarkdownRenderer

# Include CSS in head
Head(
    *EidosHeaders(),
    MarkdownCSS()
)

# Render markdown
Body(
    Markdown("# Hello\n\nThis is **markdown**!")
)
```

## Features

### GitHub Flavored Markdown
- Tables
- Fenced code blocks
- Strikethrough
- Task lists
- Autolinks

### GitHub-style Alerts

```markdown
> [!NOTE]
> Helpful information

> [!TIP]
> Helpful advice

> [!IMPORTANT]  
> Key information

> [!WARNING]
> Potential problem

> [!CAUTION]
> Danger zone
```

### Theme Integration
Automatically uses EidosUI CSS variables for consistent styling.

## Advanced Usage

### Custom Renderer

```python
from eidos.plugins.markdown import MarkdownRenderer

# Create with custom extensions
renderer = MarkdownRenderer(
    extensions=[
        'fenced_code',
        'tables',
        'toc',  # Table of contents
        MyCustomExtension()
    ]
)

# Render markdown
html = renderer.render("# Content")
```

### Direct HTML

```python
from eidos.plugins.markdown import MarkdownRenderer
import air

renderer = MarkdownRenderer()
html = renderer.render("# Hello")

# Use in Air component
Div(air.RawHTML(html))
```

## CSS Classes

All elements get `eidos-md-*` classes:

- `eidos-md` - Container
- `eidos-md-h1` - Headings  
- `eidos-md-p` - Paragraphs
- `eidos-md-code` - Code blocks
- `eidos-md-table` - Tables
- `eidos-md-alert-*` - Alert boxes

Override with custom CSS.