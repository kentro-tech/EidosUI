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

### GitHub Flavored Markdown

All standard GFM features are supported:

```python
markdown_text = """
# Headings

## Tables

| Feature | Supported |
|---------|-----------|
| Tables | ✓ |
| Task Lists | ✓ |
| Strikethrough | ✓ |

## Task Lists

- [x] Completed task
- [ ] Pending task

## Code Blocks

```python
def hello():
    return "Syntax highlighted!"
```

## ~~Strikethrough~~
"""

rendered = Markdown(markdown_text)
```

### GitHub-Style Alerts

The plugin includes support for GitHub-style alert blocks:

```markdown
> [!NOTE]
> Useful information that users should know.

> [!TIP]
> Helpful advice for doing things better.

> [!IMPORTANT]
> Key information users need to know.

> [!WARNING]
> Urgent info that needs immediate attention.

> [!CAUTION]
> Advises about risks or negative outcomes.
```

### Syntax Highlighting

Code blocks are automatically syntax highlighted:

````python
markdown_with_code = """
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

```javascript
const greeting = (name) => {
    return `Hello, ${name}!`;
};
```
"""

Markdown(markdown_with_code)
````

### Theme Integration

The markdown plugin automatically adapts to your EidosUI theme:

```python
# Light theme
Html(data_theme="light", Body(Markdown(content)))

# Dark theme  
Html(data_theme="dark", Body(Markdown(content)))

# Custom theme
Html(data_theme="my-brand", Body(Markdown(content)))
```

## Advanced Usage

### Custom Extensions

Add custom markdown extensions:

```python
from eidos.plugins.markdown import Markdown
import markdown

# Use with Python-Markdown extensions
content = Markdown(
    text,
    extensions=['extra', 'codehilite', 'toc']
)

# With custom extension instances
from my_extension import MyExtension

content = Markdown(
    text,
    extensions=['extra', MyExtension()]
)
```

### Configuration Options

```python
# Full configuration
content = Markdown(
    text,
    extensions=['extra', 'codehilite'],
    extension_configs={
        'codehilite': {
            'css_class': 'highlight',
            'linenums': True
        }
    }
)
```

### Custom CSS Classes

Add custom classes to the rendered markdown:

```python
content = Div(
    Markdown(text),
    class_="prose prose-lg max-w-none"
)
```

## Styling

### CSS Variables

The markdown plugin uses EidosUI's CSS variables:

```css
/* Headings */
.eidos-markdown h1 {
    color: var(--eidos-text-primary);
    font-size: var(--eidos-text-4xl);
}

/* Code blocks */
.eidos-markdown pre {
    background: var(--eidos-bg-secondary);
    border: 1px solid var(--eidos-border-color);
}

/* Links */
.eidos-markdown a {
    color: var(--eidos-primary);
}
```

### Custom Styling

Override specific markdown styles:

```css
/* Custom markdown styles */
.my-markdown h1 {
    border-bottom: 2px solid var(--eidos-primary);
    padding-bottom: 0.5rem;
}

.my-markdown blockquote {
    border-left: 4px solid var(--eidos-primary);
    padding-left: 1rem;
}
```

```python
Div(
    Markdown(content),
    class_="my-markdown"
)
```

## Component Reference

### Markdown Component

```python
Markdown(
    source: str,
    extensions: list = None,
    extension_configs: dict = None,
    **kwargs
) -> HTML
```

**Parameters:**
- `source`: Markdown text to render
- `extensions`: List of markdown extensions
- `extension_configs`: Configuration for extensions
- `**kwargs`: Additional HTML attributes

### MarkdownCSS Component

```python
MarkdownCSS() -> Link
```

Returns a `<link>` tag for markdown styles.

## Common Patterns

### Blog Post

```python
def BlogPost(title, date, content):
    return Article(
        Header(
            H1(title),
            Time(date, datetime=date)
        ),
        Div(
            Markdown(content),
            class_="prose max-w-none"
        )
    )
```

### Documentation Page

```python
def DocPage(content, toc=True):
    if toc:
        # Extract TOC from markdown
        html = Markdown(content, extensions=['toc'])
        # ... extract and display TOC
    else:
        html = Markdown(content)
    
    return Main(
        html,
        class_="documentation"
    )
```

### Markdown Editor Preview

```python
def MarkdownEditor():
    return Div(
        Div(
            Textarea(
                placeholder="Write markdown here...",
                oninput="updatePreview(this.value)"
            ),
            class_="w-1/2"
        ),
        Div(
            id="preview",
            class_="w-1/2"
        ),
        class_="flex gap-4"
    )
```

## File Handling

### Loading Markdown Files

```python
def load_markdown_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return Markdown(content)

# Usage
@app.get("/docs/{page}")
def docs(page: str):
    return layout(
        "Documentation",
        load_markdown_file(f"docs/{page}.md")
    )
```

### Front Matter Support

```python
import frontmatter

def load_post(filepath):
    post = frontmatter.load(filepath)
    
    return BlogPost(
        title=post['title'],
        date=post['date'],
        content=Markdown(post.content)
    )
```

## Performance Tips

### Caching Rendered Content

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def render_markdown_cached(content_hash):
    return Markdown(content)

def render_markdown(content):
    content_hash = hash(content)
    return render_markdown_cached(content_hash)
```

### Lazy Loading

```python
def LazyMarkdown(content_url):
    return Div(
        data_url=content_url,
        data_load="markdown",
        class_="markdown-placeholder"
    )
```

## Security Considerations

The markdown plugin sanitizes output by default, but be aware:

```python
# Safe: User content is sanitized
user_content = get_user_input()
safe_html = Markdown(user_content)

# If you need raw HTML (use with caution)
trusted_content = get_admin_content()
html_with_raw = Markdown(
    trusted_content,
    extensions=['extra', 'raw_html']
)
```

## Troubleshooting

### Missing Styles

Ensure you've included MarkdownCSS:

```python
Head(
    *EidosHeaders(),
    MarkdownCSS()  # Don't forget this!
)
```

### Extension Conflicts

Some extensions may conflict. Load them in the correct order:

```python
# Good order
extensions = ['extra', 'codehilite', 'toc']

# May cause issues
extensions = ['toc', 'extra', 'codehilite']
```

### Theme Not Applying

Check that your HTML has the correct theme attribute:

```python
Html(data_theme="light")  # or "dark"
```

## Examples

### Complete Example

```python
from eidos.plugins.markdown import Markdown, MarkdownCSS
from eidos.tags import *
import air

app = air.Air()

@app.get("/")
def home():
    markdown_content = """
# Welcome to My Site

This is a **markdown** powered page with:

> [!TIP]
> EidosUI makes beautiful markdown easy!

## Features

- Clean typography
- Syntax highlighting
- Theme support

```python
print("Hello, EidosUI!")
```
"""
    
    return Html(
        Head(
            *EidosHeaders(),
            MarkdownCSS(),
            Title("Markdown Demo")
        ),
        Body(
            NavBar(
                A("Home", href="/"),
                A("Docs", href="/docs"),
                lcontents=H3("My Site")
            ),
            Main(
                Markdown(markdown_content),
                class_="max-w-4xl mx-auto p-8"
            )
        )
    )
```

## Next Steps

- [Create custom markdown extensions](markdown-extension-guide.md)
- [Explore the plugin source code](https://github.com/isaac-flath/EidosUI/tree/main/eidos/plugins/markdown)
- [Learn about other plugins](index.md)