# EidosUI Markdown Rendering

Welcome to the **EidosUI Markdown plugin** demonstration! This plugin provides beautiful, theme-aware markdown rendering that automatically adapts to your color scheme.

## Features Overview

The markdown plugin supports all standard markdown features while seamlessly integrating with EidosUI's theming system:

- **Automatic theme integration** - Uses CSS variables for consistent styling
- **Zero configuration** - Works out of the box with sensible defaults
- **Extensible design** - Easy to add custom features
- **Lightweight** - Minimal dependencies

## Typography Examples

### Text Formatting

You can use standard markdown formatting:
- **Bold text** for emphasis
- *Italic text* for subtle emphasis
- ***Bold and italic*** for strong emphasis
- ~~Strikethrough~~ for deletions
- `inline code` for technical terms

### Paragraphs and Line Breaks

This is a regular paragraph. It flows naturally and respects the theme's typography settings.

This is another paragraph after a blank line. The spacing between paragraphs is controlled by EidosUI's CSS variables, ensuring consistent vertical rhythm throughout your application.

## Code Examples

### Inline Code

Use backticks for `inline code`, which is great for mentioning `function_names()`, `variables`, or `commands`.

### Code Blocks

```python
# Python example with syntax highlighting
def greet(name: str) -> str:
    """Generate a personalized greeting."""
    return f"Hello, {name}! Welcome to EidosUI."

# Usage
message = greet("Developer")
print(message)
```

```javascript
// JavaScript example
const toggleTheme = () => {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
};
```

```css
/* CSS with EidosUI variables */
.custom-component {
    background-color: var(--color-surface);
    color: var(--color-text);
    padding: var(--space-md);
    border-radius: var(--radius-md);
}
```

## Lists

### Unordered Lists

- First level item
- Another first level item
  - Nested item
  - Another nested item
    - Deeply nested item
- Back to first level

### Ordered Lists

1. First step in the process
2. Second step with substeps:
   1. Substep A
   2. Substep B
   3. Substep C
3. Final step

### Mixed Lists

1. Ordered item one
   - Unordered subitem
   - Another unordered subitem
2. Ordered item two
   - More subitems
     1. Can nest ordered in unordered
     2. As deeply as needed

## Blockquotes

> "The best way to predict the future is to invent it."
> — Alan Kay

Blockquotes can also contain multiple paragraphs:

> This is the first paragraph of a multi-paragraph quote.
>
> This is the second paragraph. Notice how the quote styling is maintained across paragraphs.
>
> You can even include **formatted text** and `code` within quotes.

## Tables

Tables automatically adapt to the theme:

| Feature | Description | Status |
|---------|-------------|--------|
| Markdown Rendering | Convert markdown to themed HTML | ✅ Complete |
| Theme Integration | Uses CSS variables | ✅ Complete |
| Syntax Highlighting | Code block highlighting | 🚧 Coming Soon |
| Table of Contents | Auto-generated TOC | 🚧 Coming Soon |
| GitHub Alerts | Note/Warning boxes | 🚧 Coming Soon |

### Complex Table Example

| Component | Props | Description | Example |
|-----------|-------|-------------|---------|
| `Markdown` | `content: str` | Main component | `Markdown("# Hello")` |
| `MarkdownCSS` | None | CSS link component | `MarkdownCSS()` |
| `MarkdownRenderer` | `extensions: list` | Core renderer | `MarkdownRenderer()` |

## Links and References

- [EidosUI Documentation](https://github.com/eidos/ui)
- [Markdown Specification](https://commonmark.org)
- [Python Markdown Extensions](https://python-markdown.github.io/extensions/)

You can also use reference-style links:

The [EidosUI][1] project provides [beautiful components][2] for modern web applications.

[1]: https://github.com/eidos/ui "EidosUI on GitHub"
[2]: https://eidos.ui/components "Component Gallery"

## Images

While images aren't included in this demo, they work seamlessly:

```markdown
![Alt text](image-url.png "Optional title")
```

Images are automatically styled with:
- Responsive sizing (`max-width: 100%`)
- Rounded corners using theme variables
- Proper spacing

## Horizontal Rules

Use three or more hyphens, asterisks, or underscores:

---

The horizontal rule above uses the theme's border color and spacing.

## Advanced Features (Coming Soon)

### GitHub-Style Alerts

Once implemented, you'll be able to use:

```markdown
> [!NOTE]
> Useful information that users should know.

> [!WARNING]
> Critical content demanding user attention.
```

### Table of Contents

The TOC extension will automatically generate navigation from your headers:
- Automatic ID generation
- Nested structure support
- Scrollspy integration
- Customizable styling

### Custom Extensions

The plugin architecture makes it easy to add your own extensions:

```python
class CustomExtension:
    def process(self, text: str) -> str:
        # Your custom processing logic
        return processed_text
```

## Summary

The EidosUI Markdown plugin provides a powerful, theme-aware markdown rendering solution that:

1. **Integrates seamlessly** with your existing EidosUI application
2. **Requires zero configuration** to get started
3. **Respects your theme** automatically
4. **Remains extensible** for custom needs

Whether you're building documentation, blog posts, or any content-heavy application, the markdown plugin ensures your content looks great in any theme.

---

*This example showcases the current capabilities of the EidosUI Markdown plugin MVP.*