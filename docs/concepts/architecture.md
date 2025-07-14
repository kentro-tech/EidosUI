# Architecture

EidosUI follows a layered architecture. Each layer builds on the previous.

## Layers


### The Stylistic Base

#### CSS Variables

Themes are defined as a bunch of css variables in a css file (like `color-primary` and `color-primary-hover`)

```css
[data-theme="light"] {
    /* Core Colors */
    --color-primary: #3b82f6;
    --color-primary-hover: #2563eb;
    ...
}
```

#### CSS Classes

Those css variables are used in a style sheet to define classes (like `eidos-h1`)

```css
.eidos-h1 {
    font-size: var(--font-size-3xl);
    font-weight: var(--font-weight-bold);
    line-height: var(--line-height-tight);
    margin-bottom: var(--space-md);
}
```

### The Python Exposure

#### Style Classes

CSS classes are exposed in python classes like so:

```python
class Typography:
    h1: Final[str] = "eidos-h1"
    h2: Final[str] = "eidos-h2"
    ...
```

#### Tags

Which are the used to create `AirTag` components.

```python
def H1(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)
```

### The more complex features

#### Components

Complex UI built from styled tags:

```python
class DataTable:
    @classmethod
    def from_lists(cls, data, headers=None):
        # Build table from tags
```

Located in `/eidos/components/`.

### Plugins

Things that do not fit well into any of the above but are still useful are optional plugins to install (like the `markdown` plugin)


#### Plugins

Things that do not fit well into any of the above but are still useful are optional plugins to install (like the `markdown` plugin)