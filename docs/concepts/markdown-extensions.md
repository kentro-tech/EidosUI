# Markdown Extensions

Extend the markdown renderer with custom syntax.

## Built-in Extensions

### GitHub Alerts

```markdown
> [!NOTE]
> Useful information

> [!WARNING]  
> Important warning
```

Supported types: NOTE, TIP, IMPORTANT, WARNING, CAUTION

### Standard Extensions

- `fenced_code` - Code blocks with ` ``` `
- `tables` - Markdown tables
- `nl2br` - Newline to `<br>`
- `sane_lists` - Better list handling

## Custom Extensions

### Example: Mentions

Convert `@username` to links:

```python
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor
import xml.etree.ElementTree as etree

class MentionPattern(SimpleTagInlineProcessor):
    def handleMatch(self, m, data):
        username = m.group(1)
        
        link = etree.Element('a')
        link.set('href', f'/user/{username}')
        link.set('class', 'mention-link')
        
        span = etree.Element('span')
        span.set('class', 'mention')
        span.text = f'@{username}'
        
        link.append(span)
        return link, m.start(0), m.end(0)

class MentionExtension(Extension):
    def extendMarkdown(self, md):
        pattern = MentionPattern(r'@(\w+)', md)
        md.inlinePatterns.register(pattern, 'mention', 160)
```

### Using Extensions

```python
from eidos.plugins.markdown import MarkdownRenderer

renderer = MarkdownRenderer(
    extensions=[
        'fenced_code',
        'tables', 
        MentionExtension()
    ]
)

html = renderer.render("Hello @alice!")
```

## Extension Types

### Inline Patterns
Process inline elements (bold, links, mentions).

### Block Processors
Process block elements (paragraphs, lists).

### Tree Processors
Modify the element tree after parsing.

### Preprocessors
Modify text before parsing.

### Postprocessors
Modify HTML after rendering.

## Tips

- Use `SimpleTagInlineProcessor` for simple replacements
- Set appropriate priority (100-200 range)
- Test with edge cases
- Return `None` to skip matches