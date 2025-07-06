# EidosUI 🎨

A modern, flexible Tailwind CSS-based UI library for Python web frameworks. Built for maximum developer flexibility while providing excellent defaults.

> [!CAUTION]
> This library is not ready for anything yet.  IN fact, this readme is more of design ideas than anything as much of what's in here isn't implemented yet!


## Design

### Base CSS

- `styles.css` : defines all the core css logic to create classes like `edios-mark`, `eidos-small`, etc.
- `light.css`/`dark.css` : These define lots of css variables used in `styles.css` and are themes

Users would create a custom theme by copying light/dark css files and changing the variable definitions.

### Styles

This has enums that make the Base CSS clases accessible in python.  For example:

`styles.typography.h1` or `styles.buttons.primary`

### Tags

```python
def H1(*content, cls: str = None, **kwargs) -> air.H1:
    """Semantic H1 heading"""
    return air.H1(*content, cls=stringify(styles.typography.h1, cls), **kwargs)

def Mark(*content, cls: str = None, **kwargs) -> air.Mark:
    """Highlighted text"""
    return .Mark(*content, cls=stringify(styles.typography.mark, cls), **kwargs)

def Small(*content, cls: str = , **kwargs) -> air.Small:
    """Small text"""
    return air.Small(*content, cls=stringify(styles.typography.small, cls), **kwargs) 
```

### Components (Not Built Yet)

Theses are things that go beyond just exposing css to python.  Here's a simple example of what might be added.

```python
class Table:
    def __init__(self, cls: str = None, **kwargs):
        """Create an empty table with optional styling"""
        self.cls = cls
        self.kwargs = kwargs
    
    @classmethod
    def from_lists(cls, data: list[list], headers: list[str] = None, cls_: str = None, **kwargs):
        """Create table from list of lists"""
        thead = []
        if headers:
            thead = THead(Tr(*[Th(header) for header in headers]))
        
        tbody_rows = []
        for data in row_data:
            tbody_rows.append(Tr(*map(Td, row_data)))
        tbody = TBody(*tbody_rows)
        
        return Table(thead+tbody, cls=cls_, **kwargs)
    
    @classmethod
    def from_dicts(cls, data: list[dict], headers: list[str] = None, cls_: str = None, **kwargs):
        """Create table from list of dictionaries"""
        thead = []
        if headers:
            thead = THead(Tr(*[Th(header) for header in headers]))
        
        tbody_rows = []
        for row in data:
            tbody_rows.append(Tr(*[Td(row.get(header, "")) for header in (headers or list(row.keys()))]))
        tbody = TBody(*tbody_rows)
        
        return Table(thead+tbody, cls=cls_, **kwargs)

# Usage examples:
Table.from_lists([["A", "B"], ["C", "D"]], headers=["Col1", "Col2"])
Table.from_dicts([{"name": "John", "age": 25}], headers=["Name", "Age"])
```

## Plugins

### edios-md

This will be installable with `pip install "eidos[markdown]"`. 

This is a plugin for rendering markdown that is well scoped to just markdown rendering.  This module does markdown rendering well with table of contents with scrollspy, code highlighting, latex rendering, etc.  It must be used with `EidosUI` as it uses css variables from there for the styling (so it is always in sync with the theme)

