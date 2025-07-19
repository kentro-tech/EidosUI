# EidosUI Markdown Plugin Guide

This guide covers everything you need to know about using markdown in EidosUI: basic usage, built-in extensions, and creating custom extensions.

> **⚠️ Security Warning**
> 
> The EidosUI markdown plugin renders raw HTML without sanitization to support advanced features like forms, embeds, and custom styling. **Never render untrusted user content** without proper sanitization. If you need to display user-generated content, consider:
> - Using a separate HTML sanitizer like `bleach` after rendering
> - Restricting markdown features for untrusted content
> - Rendering untrusted content in a sandboxed iframe
> 
> This design choice prioritizes flexibility for developers who control their content.

## Installation

Install the markdown plugin with:

```bash
pip install "eidosui[markdown]"
```

## Basic Usage

### Step 1: Import Required Components

```python
from eidos.plugins.markdown import Markdown, MarkdownCSS, MarkdownRenderer
```

### Step 2: Include CSS in Your Page

```python
from eidos import *

Html(
    Head(
        *EidosHeaders(),
        MarkdownCSS()  # Required for styling
    ),
    Body(
        # Your content here
    )
)
```

### Step 3: Render Markdown

```python
Body(
    Markdown("# Hello World\n\nThis is **markdown**!")
)
```
## Using Extensions

### Default Extensions

The plugin includes these extensions by default:

- `fenced_code` - Code blocks with ` ``` `
- `tables` - Markdown tables
- `nl2br` - Newline to `<br>`
- `sane_lists` - Better list handling
- GitHub alerts (custom)

### Adding Standard Extensions

```python
from eidos.plugins.markdown import MarkdownRenderer

# Create renderer with additional extensions
renderer = MarkdownRenderer(
    extensions=[
        'fenced_code',
        'tables',
        'toc',          # Table of contents
        'footnotes',    # Footnote support
        'attr_list',    # Add attributes to elements
    ]
)

# Render markdown
html = renderer.render("# My Content")

# Use in your page
from air import RawHTML

Body(
    Div(RawHTML(html), class_="eidos-md")
)
```

## Creating Custom Extensions

Let's create two simple extensions: mentions (@username) and emoji shortcuts (:smile:).


> ![TIP]
> See [the markdown extension example](https://github.com/kentro-tech/EidosUI/tree/main/examples/markdown_extension) for the full working example


### Step 1: Create a Mention Extension

```python
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown.util import AtomicString
import xml.etree.ElementTree as etree

class MentionPattern(SimpleTagInlineProcessor):
    """Converts @username to a styled mention link."""
    
    def handleMatch(self, m, data):
        """Handle the pattern match."""
        username = m.group(1)
        
        # Create a link element
        link = etree.Element('a')
        link.set('href', f'/user/{username}')
        link.set('class', 'mention-link')
        
        # Create the span inside the link
        span = etree.Element('span')
        span.set('class', 'mention')
        span.text = AtomicString(f'@{username}')
        
        link.append(span)
        
        return link, m.start(0), m.end(0)

class MentionExtension(Extension):
    """Extension that adds @mention support."""
    
    def extendMarkdown(self, md):
        # Add the mention pattern: @username
        mention_pattern = MentionPattern(r'@(\w+)', md)
        md.inlinePatterns.register(mention_pattern, 'mention', 160)
```

### Step 2: Create an Emoji Extension

```python
from markdown.inlinepatterns import InlineProcessor

class EmojiPattern(InlineProcessor):
    """Converts :emoji: shortcuts to actual emojis."""
    
    EMOJI_MAP = {
        'smile': '😊',
        'heart': '❤️',
        'star': '⭐',
        'fire': '🔥',
        'rocket': '🚀',
        'check': '✅',
        'x': '❌',
        'warning': '⚠️',
        'info': 'ℹ️',
        'bulb': '💡',
    }
    
    def handleMatch(self, m, data):
        """Handle the pattern match."""
        emoji_name = m.group(1)
        
        if emoji_name in self.EMOJI_MAP:
            el = etree.Element('span')
            el.set('class', 'emoji')
            el.text = self.EMOJI_MAP[emoji_name]
            return el, m.start(0), m.end(0)
        
        # If emoji not found, return None
        return None, None, None

class EmojiExtension(Extension):
    """Extension that adds :emoji: support."""
    
    def extendMarkdown(self, md):
        emoji_pattern = EmojiPattern(r':(\w+):', md)
        md.inlinePatterns.register(emoji_pattern, 'emoji', 170)
```

### Step 3: Use Your Extensions

```python
from eidos.plugins.markdown import MarkdownRenderer

# Create renderer with custom extensions
renderer = MarkdownRenderer(
    extensions=[
        MentionExtension(),
        EmojiExtension(),
    ]
)

# Render markdown with custom syntax
html = renderer.render("""
# Hello @alice!

Great work on this feature! :star: :fire:

Hey @team, check out this :rocket: fast implementation!
""")
```

### Step 4: Add Custom Styles

```css
/* Custom styles for mentions */
.mention-link {
    text-decoration: none;
}

.mention {
    background: var(--color-primary-light);
    color: var(--color-primary);
    padding: 0.125rem 0.375rem;
    border-radius: 0.25rem;
    font-weight: 500;
}

.mention:hover {
    background: var(--color-primary);
    color: white;
}

/* Custom styles for emojis */
.emoji {
    font-size: 1.2em;
}
```