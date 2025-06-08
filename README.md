# EidosUI 🎨

A modern, flexible Tailwind CSS-based UI library for Python web frameworks. Built for maximum developer flexibility while providing excellent defaults.


## Abstractions

- **Themes:** A Theme is a series of CSS variables.  See `theme/dark.css` and `theme/light.css` for examples
- **Theme Switching** is done in `static/eidos-ui.js` this is all AI generated and not looked at yet so probably bad
- **Styles** are in `styles.py` where we define data classes based on the css variables defined in the themes.  These are a collection of class strings.
- **components** are fasttags that FT components by default.  For example

```python
def H1(*content, cls: str = typography_styles.h1, **kwargs) -> ft.H1:
    """Semantic H1 heading"""
    return ft.H1(*content, cls=cls, **kwargs)

def Mark(*content, cls: str = typography_styles.mark, **kwargs) -> ft.Mark:
    """Highlighted text"""
    return ft.Mark(*content, cls=cls, **kwargs)


def Small(*content, cls: str = typography_styles.small, **kwargs) -> ft.Small:
    """Small text"""
    return ft.Small(*content, cls=cls, **kwargs) 
```