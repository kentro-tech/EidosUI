# Markdown Plugin

The EidosUI Markdown plugin provides beautiful, theme-aware markdown rendering with support for GitHub Flavored Markdown and custom extensions.

## Installation

```bash
pip install "eidosui[markdown]"
```

## Quick Start

```python
from eidos.plugins.markdown import Markdown, MarkdownCSS

# Include CSS in your HTML head
Head(
    *EidosHeaders(),
    MarkdownCSS()  # Markdown-specific styles
)

# Render markdown
content = Markdown("""
# Welcome to EidosUI Markdown

This plugin provides **beautiful** markdown rendering with:

- Full GitHub Flavored Markdown support
- Syntax highlighting
- Theme awareness
- Custom extensions
""")
```

## Features

## Extension Guide
