# Philosophy & Architecture

## Principles

### 1. Semantic HTML

HTML elements have meaning. EidosUI enhances them:

```python
# Not this
Div("Important text", class_="text-bold text-lg")

# This
Strong("Important text")  # Semantic AND styled
```

### 2. Progressive Enhancement

Start with HTML. Add styling. Add behavior:

```python
# Basic
Button("Submit")

# Styled
Button("Submit", class_=styles.buttons.primary)

# Interactive
Button("Submit", class_=styles.buttons.primary, hx_post="/api/submit")
```

### 3. CSS Variables

```css
.eidos-button {
    background: var(--eidos-primary);
    color: var(--eidos-primary-text);
}
```

Enables runtime theming.

### 4. Python API

```python
NavBar(
    A("Home", href="/"),
    sticky=True,
    scrollspy=True
)
```

Type-safe. IDE-friendly. Composable.

## Architecture

### Layers

```
┌─────────────────────────────────┐
│      Your Application           │ 
├─────────────────────────────────┤
│      Components                 │  Complex patterns
├─────────────────────────────────┤
│      Tags                       │  Styled HTML elements
├─────────────────────────────────┤
│      Styles                     │  CSS class access
├─────────────────────────────────┤
│      CSS System                 │  Variables & themes
└─────────────────────────────────┘
```

### CSS Structure

**Base (`styles.css`)**
```css
.eidos-h1 {
    font-size: var(--eidos-text-4xl);
    color: var(--eidos-text-primary);
}
```

**Themes (`light.css`, `dark.css`)**
```css
:root {
    --eidos-text-primary: #1a202c;
    --eidos-bg-primary: #ffffff;
}

[data-theme="dark"] {
    --eidos-text-primary: #f7fafc;
    --eidos-bg-primary: #1a202c;
}
```

### Component Structure

**Level 1: Tags**
```python
def H1(*content, cls=None, **kwargs):
    return air.H1(*content, cls=stringify(styles.typography.h1, cls), **kwargs)
```

**Level 2: Components**
```python
def Card(title, content, footer=None):
    return Article(
        Header(H3(title)),
        Section(content),
        Footer(footer) if footer else None,
        class_="eidos-card"
    )
```

## Design Decisions

### Why CSS Variables?

- Runtime theme switching
- No build step
- User customization
- Browser native

### Why Not Web Components?

- Server-side rendering
- No JavaScript required
- Better SEO
- Simpler Python integration

### Why Both Tailwind and Custom Classes?

- Tailwind: Layout flexibility
- Custom classes: Component consistency

## Extension Points

1. Custom components
2. Style extensions
3. Theme creation
4. Plugin development

## Performance

- CSS-only features when possible
- Server-side rendering
- Minimal JavaScript
- No virtual DOM