# Architecture

EidosUI is the UI component library for [Air](https://airwebframework.org). Its architecture reflects a core belief: developers should be able to use Python (Air tags) or Jinja templates interchangeably, with identical results.

## The Problem We're Solving

Air supports two ways to write HTML:

- **Air tags**: Python objects like `air.Div(air.H1("Hello"))`
- **Jinja templates**: Traditional HTML templates with `{{ variables }}`

Most UI libraries pick one. EidosUI picks both. A team where one developer prefers Python and another prefers Jinja should be able to work on the same codebase without friction or conversion.

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                   CSS Layer                     │
│        (Variables, Classes, Structures)         │
│              The Source of Truth                │
└─────────────────────┬───────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
┌───────────────────┐     ┌───────────────────┐
│    Python API     │     │     Jinja API     │
│                   │     │                   │
│  eidos.Card(...)  │     │ {% call card() %} │
│  eidos.Button()   │     │  {{ button() }}   │
└───────────────────┘     └───────────────────┘
        │                           │
        └─────────────┬─────────────┘
                      ▼
               Same HTML output
               Same visual result
```

Both APIs are equal frontends to the same CSS foundation. Neither is a wrapper around the other.

## Layer 1: CSS Foundation

The CSS layer is the source of truth. Everything else just applies it.

### CSS Variables

Themes are defined as CSS custom properties. Switching themes means switching which variables are active.

```css
[data-theme="light"] {
    --color-primary: #3b82f6;
    --color-primary-hover: #2563eb;
    --color-background: #ffffff;
    --color-text: #1f2937;
    --space-md: 1rem;
    --font-size-3xl: 1.875rem;
}

[data-theme="dark"] {
    --color-primary: #60a5fa;
    --color-primary-hover: #93c5fd;
    --color-background: #111827;
    --color-text: #f9fafb;
    /* Same spacing and sizing, different colors */
}
```

### CSS Classes

Classes consume variables to define reusable styles:

```css
.eidos-h1 {
    font-size: var(--font-size-3xl);
    font-weight: var(--font-weight-bold);
    line-height: var(--line-height-tight);
    margin-bottom: var(--space-md);
}

.eidos-btn {
    padding: var(--space-sm) var(--space-md);
    background: var(--color-primary);
    color: var(--color-text-inverse);
    border-radius: var(--radius-md);
}

.eidos-btn:hover {
    background: var(--color-primary-hover);
}
```

### Component Structures

Complex components have documented HTML structures that both APIs must produce:

```html
<!-- Card structure -->
<div class="eidos-card">
    <div class="eidos-card-header">Title here</div>
    <div class="eidos-card-body">Content here</div>
    <div class="eidos-card-footer">Actions here</div>
</div>
```

This structure is the contract. Both Python and Jinja implementations must output this exact HTML.

## Layer 2: Python API

For developers who prefer writing Python.

### Style References

CSS class names exposed as Python constants for IDE autocomplete and typo prevention:

```python
class Typography:
    h1: Final[str] = "eidos-h1"
    h2: Final[str] = "eidos-h2"
    h3: Final[str] = "eidos-h3"

class Buttons:
    base: Final[str] = "eidos-btn"
    primary: Final[str] = "eidos-btn-primary"
    secondary: Final[str] = "eidos-btn-secondary"
```

### Styled Tags

Simple wrappers that apply EidosUI classes to Air tags:

```python
def H1(*content: Any, class_: str | list[str] | None = None, **kwargs: Any) -> air.Tag:
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)

def Button(*content: Any, variant: str = "primary", **kwargs: Any) -> air.Tag:
    cls = stringify(styles.buttons.base, getattr(styles.buttons, variant))
    return air.Button(*content, class_=cls, **kwargs)
```

### Components

Complex UI assembled from styled tags:

```python
def Card(
    *body: Any,
    title: str | None = None,
    footer: Any | None = None,
    **kwargs: Any
) -> air.Tag:
    children = []
    if title:
        children.append(air.Div(title, class_=styles.card.header))
    children.append(air.Div(*body, class_=styles.card.body))
    if footer:
        children.append(air.Div(footer, class_=styles.card.footer))
    return air.Div(*children, class_=styles.card.base, **kwargs)
```

## Layer 2: Jinja API

For developers who prefer writing templates.

### Macros

Jinja macros mirror the Python component API:

```jinja
{% macro card(title=None, footer=None) %}
<div class="eidos-card">
    {% if title %}
    <div class="eidos-card-header">{{ title }}</div>
    {% endif %}
    <div class="eidos-card-body">{{ caller() }}</div>
    {% if footer %}
    <div class="eidos-card-footer">{{ footer }}</div>
    {% endif %}
</div>
{% endmacro %}

{% macro button(variant="primary") %}
<button class="eidos-btn eidos-btn-{{ variant }}">{{ caller() }}</button>
{% endmacro %}
```

### Usage

Import macros and call them:

```jinja
{% from "eidos/macros.html" import card, button %}

{% call card(title="Welcome") %}
    <p>This is the card body.</p>
    {% call button(variant="primary") %}Click me{% endcall %}
{% endcall %}
```

## The Parity Guarantee

These two code samples must produce identical HTML:

**Python:**
```python
eidos.Card(
    eidos.P("This is the card body."),
    eidos.Button("Click me", variant="primary"),
    title="Welcome"
)
```

**Jinja:**
```jinja
{% call card(title="Welcome") %}
    <p>This is the card body.</p>
    {% call button(variant="primary") %}Click me{% endcall %}
{% endcall %}
```

**Output (both):**
```html
<div class="eidos-card">
    <div class="eidos-card-header">Welcome</div>
    <div class="eidos-card-body">
        <p>This is the card body.</p>
        <button class="eidos-btn eidos-btn-primary">Click me</button>
    </div>
</div>
```

This is testable. EidosUI's test suite verifies that Python and Jinja implementations produce matching output.

## Layer 3: Plugins

Optional extensions for features that don't belong in core:

- **markdown**: Styled markdown rendering
- **code**: Syntax highlighting for code blocks
- **icons**: Icon library integration

Plugins follow the same dual-API pattern when applicable.

## Why This Architecture?

**No framework lock-in.** EidosUI owns its CSS. No Tailwind, no DaisyUI, no external dependencies that might change or disappear.

**AI-friendly.** Following Air's philosophy, both APIs are predictable. `eidos.Card(title="X")` and `{% call card(title="X") %}` do exactly what they look like. An LLM can generate correct code without guessing.

**Team flexibility.** Different developers have different preferences. This architecture makes that a non-issue.

**Minimal footprint.** Just CSS and thin API layers. No JavaScript framework, no build step, no complexity beyond what's needed.

## Acknowledgments

EidosUI was created by [Isaac Flath](https://github.com/Isaac-Flath), who also created [MonsterUI](https://github.com/AnswerDotAI/MonsterUI). MonsterUI proved that Python developers could have a professional styling system without leaving their language. EidosUI continues that work with a new foundation: owning its CSS entirely and treating Jinja templates as equal to Python.
