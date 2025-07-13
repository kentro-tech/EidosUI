# Architecture

EidosUI follows a layered architecture. Each layer builds on the previous.

## Layers

### 1. CSS Variables

Base layer defining design tokens:

```css
--color-primary: #3b82f6;
--font-size-lg: 1.125rem;
--space-md: 1rem;
```

Located in `/eidos/css/themes/`.

### 2. CSS Classes  

Classes using CSS variables:

```css
.eidos-h1 {
    font-size: var(--font-size-3xl);
    margin-bottom: var(--space-md);
}
```

Located in `/eidos/css/styles.css`.

### 3. Style Enums

Python classes exposing CSS classes:

```python
class Typography:
    h1: Final[str] = "eidos-h1"
```

Located in `/eidos/styles.py`.

### 4. Styled Tags

Air tags with default styling:

```python
def H1(*content, class_=None, **kwargs):
    return air.H1(
        *content, 
        class_=stringify(styles.typography.h1, class_), 
        **kwargs
    )
```

Located in `/eidos/tags.py`.

### 5. Components

Complex UI built from styled tags:

```python
class DataTable:
    @classmethod
    def from_lists(cls, data, headers=None):
        # Build table from tags
```

Located in `/eidos/components/`.

## Benefits

- **Customizable** - Change CSS variables, override classes
- **Predictable** - Clear data flow from CSS to Python
- **Flexible** - Use any layer directly