# EidosUI

Modern UI library for Python web frameworks. Built on Air and Tailwind CSS.

> [!CAUTION]
> This library is in alpha, and may have semi-frequent breaking changes.  I'd love for you to try it an contribute feedback or PRs!

## Installation

```bash
pip install eidosui
```

## Quick Start

```python
from eidos import *
import air

app = air.Air()

@app.get("/")
def home():
    return Html(
        Head(
            Title("My App"),
            *EidosHeaders()  # Required CSS/JS
        ),
        Body(
            H1("Welcome"),
            P("Build modern web apps with Python."),
            DataTable.from_lists(
                [["Alice", "30"], ["Bob", "25"]], 
                headers=["Name", "Age"]
            )
        )
    )

app.run()
```

## Features

- **Styled HTML tags** - Pre-styled versions of all HTML elements
- **Components** - DataTable, NavBar, and more  
- **Themes** - Light/dark themes via CSS variables
- **Type hints** - Full type annotations
- **Air integration** - Works seamlessly with Air framework

## Plugins

### Markdown

```bash
pip install "eidosui[markdown]"
```

```python
from eidos.plugins.markdown import Markdown, MarkdownCSS

Head(
    *EidosHeaders(),
    MarkdownCSS()  # Add markdown styles
)

Body(
    Markdown("# Hello\n\nSupports **GitHub Flavored Markdown**")
)
```

## Documentation

Full documentation: https://eidosui.readthedocs.io

## License

MIT