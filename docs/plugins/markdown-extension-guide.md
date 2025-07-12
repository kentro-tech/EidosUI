# Creating Markdown Extensions for EidosUI

This guide walks you through creating custom Markdown extensions for the EidosUI Markdown plugin. We'll use the GitHub-style alerts extension as a reference example.

## Understanding Markdown Extensions

EidosUI's Markdown plugin is built on Python-Markdown, which provides a powerful extension API. Extensions can:

- Add new syntax patterns
- Modify how existing syntax is rendered
- Add preprocessing or postprocessing steps
- Integrate with EidosUI's theming system

## Basic Extension Structure

Every Markdown extension follows this pattern:

```python
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
import xml.etree.ElementTree as etree

class MyProcessor(BlockProcessor):
    """Process custom markdown syntax"""
    
    def test(self, parent, block):
        """Test if this processor should handle the block"""
        return # True if this processor handles this block
    
    def run(self, parent, blocks):
        """Process the block and create HTML elements"""
        # Process the block
        # Create elements
        # Return True if processed

class MyExtension(Extension):
    """Register the processor with markdown"""
    
    def extendMarkdown(self, md):
        """Add processor to markdown instance"""
        md.parser.blockprocessors.register(
            MyProcessor(md.parser),
            'my_processor',
            priority_number
        )
```

## Step-by-Step: GitHub Alerts Extension

Let's build a GitHub-style alerts extension that transforms:

```markdown
> [!NOTE]
> This is a note alert
```

Into a styled alert box.

### 1. Define Alert Types

```python
ALERT_TYPES = {
    'NOTE': {
        'class': 'eidos-alert eidos-alert-info',
        'icon': 'ℹ️',
        'title': 'Note'
    },
    'TIP': {
        'class': 'eidos-alert eidos-alert-success',
        'icon': '💡',
        'title': 'Tip'
    },
    'WARNING': {
        'class': 'eidos-alert eidos-alert-warning',
        'icon': '⚠️',
        'title': 'Warning'
    }
}
```

### 2. Create the Block Processor

```python
import re
from markdown.blockprocessors import BlockProcessor

class AlertBlockProcessor(BlockProcessor):
    # Pattern to match > [!TYPE]
    RE_ALERT = re.compile(r'^> \[!(NOTE|TIP|WARNING)\]', re.MULTILINE)
    
    def test(self, parent, block):
        """Check if block starts with alert syntax"""
        return bool(self.RE_ALERT.match(block))
```

### 3. Process the Alert Content

```python
def run(self, parent, blocks):
    block = blocks.pop(0)
    match = self.RE_ALERT.match(block)
    
    if not match:
        return False
    
    alert_type = match.group(1)
    alert_config = self.ALERT_TYPES.get(alert_type)
    
    # Create alert container
    alert_div = etree.SubElement(parent, 'div')
    alert_div.set('class', alert_config['class'])
    
    # Add header with icon
    header = etree.SubElement(alert_div, 'div')
    header.set('class', 'eidos-alert-header')
    
    icon = etree.SubElement(header, 'span')
    icon.set('class', 'eidos-alert-icon')
    icon.text = alert_config['icon']
    
    # Process content
    content = self.RE_ALERT.sub('', block)
    # ... process remaining content
    
    return True
```

### 4. Handle Multi-line Content

```python
# Continue processing lines that are part of the alert
while blocks and blocks[0].startswith('>'):
    continuation = blocks.pop(0)
    # Process continuation lines
```

### 5. Register the Extension

```python
class AlertExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            AlertBlockProcessor(md.parser),
            'github_alerts',
            175  # Priority - before blockquote
        )
```

## CSS Integration

EidosUI extensions should use the CSS variable system for theming:

```css
.eidos-alert {
    padding: 1rem;
    border-radius: 0.5rem;
    border: 1px solid var(--eidos-border-color);
}

.eidos-alert-info {
    background: var(--eidos-info-bg);
    color: var(--eidos-info-text);
}
```

## Using Your Extension

### 1. Package Structure

```
my_extension/
├── __init__.py
├── extension.py
└── styles.css
```

### 2. Register with Markdown

```python
from eidos.plugins.markdown import Markdown
from my_extension import MyExtension

# Use with custom extensions
content = Markdown(
    text,
    extensions=['extra', MyExtension()]
)
```

### 3. Include CSS

```python
from air.tags import Link

Link(
    rel="stylesheet",
    href="/static/my_extension.css"
)
```

## Advanced Patterns

### Inline Patterns

For inline syntax like `::highlight::`:

```python
from markdown.inlinepatterns import InlineProcessor

class HighlightProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('mark')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)
```

### Tree Processors

For post-processing the entire document:

```python
from markdown.treeprocessors import Treeprocessor

class AddClassTreeprocessor(Treeprocessor):
    def run(self, root):
        for element in root.iter('table'):
            element.set('class', 'eidos-table')
```

### Preprocessors

For modifying raw text before parsing:

```python
from markdown.preprocessors import Preprocessor

class MyPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            # Modify lines
            new_lines.append(line)
        return new_lines
```

## Best Practices

### 1. Use EidosUI Classes

Always use `eidos-` prefixed classes for consistency:

```python
element.set('class', 'eidos-alert eidos-alert-info')
```

### 2. Support Theming

Use CSS variables for colors and spacing:

```css
.eidos-custom {
    color: var(--eidos-text-primary);
    background: var(--eidos-bg-secondary);
}
```

### 3. Handle Edge Cases

- Empty content
- Nested structures  
- Malformed syntax
- Multi-line content

### 4. Set Appropriate Priority

- `> 170`: Before blockquotes
- `> 90`: Before code blocks
- `< 50`: After most processors

## Example: Task List Extension

```python
class TaskListProcessor(InlineProcessor):
    """Convert [ ] and [x] to checkboxes"""
    
    PATTERN = r'\[([ x])\]'
    
    def handleMatch(self, m, data):
        checkbox = etree.Element('input')
        checkbox.set('type', 'checkbox')
        checkbox.set('disabled', 'disabled')
        
        if m.group(1) == 'x':
            checkbox.set('checked', 'checked')
            
        return checkbox, m.start(0), m.end(0)

class TaskListExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(
            TaskListProcessor(self.PATTERN, md),
            'tasklist',
            75
        )
```

## Testing Your Extension

```python
def test_alert_extension():
    md = markdown.Markdown(extensions=[AlertExtension()])
    
    text = "> [!NOTE]\n> This is a test"
    html = md.convert(text)
    
    assert 'eidos-alert' in html
    assert 'Note' in html
```

## Distribution

### PyPI Package

```python
# setup.py
setup(
    name='eidos-markdown-myextension',
    packages=['my_extension'],
    install_requires=['markdown>=3.0', 'eidosui'],
    entry_points={
        'markdown.extensions': [
            'my_extension = my_extension:MyExtension'
        ]
    }
)
```

### Usage

```bash
pip install eidos-markdown-myextension
```

```python
Markdown(text, extensions=['my_extension'])
```

## Resources

- [Python-Markdown Extension API](https://python-markdown.github.io/extensions/api/)
- [EidosUI Markdown Plugin Source](https://github.com/isaac-flath/EidosUI/tree/main/eidos/plugins/markdown)
- [Example Extensions](https://github.com/Python-Markdown/markdown/tree/master/markdown/extensions)