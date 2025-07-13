# Components

Higher-level UI components built from styled tags.

## DataTable

Create tables from data.

### From Lists

```python
from eidos import DataTable

table = DataTable.from_lists(
    data=[
        ["Alice", "30", "Engineer"],
        ["Bob", "25", "Designer"]
    ],
    headers=["Name", "Age", "Role"]
)
```

### From Dicts

```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

table = DataTable.from_dicts(data)
# Headers auto-generated from keys
```

### Custom Styling

```python
DataTable.from_lists(
    data=data,
    headers=headers,
    class_="striped",  # Add CSS class
    id="user-table"    # Add ID
)
```

## NavBar

Navigation component.

```python
from eidos import NavBar

nav = NavBar(
    brand="My App",
    items=[
        {"text": "Home", "href": "/"},
        {"text": "About", "href": "/about"}
    ]
)
```

## EidosHeaders

Required CSS/JS for EidosUI.

```python
from eidos import EidosHeaders

Head(
    Title("My App"),
    *EidosHeaders()  # Unpacks multiple tags
)
```

Includes:
- Theme CSS
- Component styles  
- JavaScript for interactivity

## Creating Components

Build your own:

```python
def Card(title, content, **kwargs):
    return Div(
        H3(title, class_="card-title"),
        Div(content, class_="card-body"),
        class_="card",
        **kwargs
    )
```

Use styled tags as building blocks.