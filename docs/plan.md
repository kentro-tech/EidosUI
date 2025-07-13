# Plan: Programmatic API Reference Generation for EidosUI

## Goal
Generate API documentation for EidosUI components and render it as HTML using EidosUI itself.

## Requirements
1. Extract docstrings, function signatures, and type hints from Python code
2. Convert to structured data
3. Render as HTML using EidosUI components
4. Display in the documentation app

## Library Options

### 1. **inspect module** (Built-in)
- Pros: No dependencies, full control
- Cons: More manual work
- Use for: Basic introspection

```python
import inspect
from eidos import tags

def get_function_info(func):
    sig = inspect.signature(func)
    doc = inspect.getdoc(func)
    return {
        'name': func.__name__,
        'signature': str(sig),
        'doc': doc,
        'params': sig.parameters
    }
```

### 2. **ast module** (Built-in)
- Pros: Parse without importing, get source code
- Cons: Complex parsing logic
- Use for: Static analysis

```python
import ast

def extract_functions(filepath):
    with open(filepath) as f:
        tree = ast.parse(f.read())
    # Extract function definitions
```

### 3. **pdoc** (Third-party)
- Pros: Powerful, minimal dependencies
- Cons: HTML output needs parsing
- Installation: `pip install pdoc`

```python
import pdoc

# Extract documentation
mod = pdoc.Module('eidos.tags')
doc = mod.docstring
functions = mod.functions()
```

### 4. **sphinx** with autodoc
- Pros: Industry standard, very powerful
- Cons: Heavy, complex setup
- Use for: Full documentation sites

### 5. **pydoc** (Built-in)
- Pros: Built-in, simple
- Cons: Limited customization
- Use for: Quick documentation

## Recommended Approach

Use **inspect + ast** for a lightweight solution:

1. Use `inspect` for runtime introspection
2. Use `ast` for source code parsing when needed
3. Build custom renderer with EidosUI

## Implementation Plan

### Step 1: Create API Extractor
```python
# api_extractor.py
import inspect
import importlib
from typing import List, Dict, Any

def extract_module_api(module_name: str) -> Dict[str, Any]:
    """Extract API info from a module"""
    module = importlib.import_module(module_name)
    
    functions = []
    classes = []
    
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(extract_function_info(obj))
        elif inspect.isclass(obj):
            classes.append(extract_class_info(obj))
    
    return {
        'module': module_name,
        'doc': inspect.getdoc(module),
        'functions': functions,
        'classes': classes
    }
```

### Step 2: Create API Renderer
```python
# api_renderer.py
from eidos.tags import *

def render_function(func_info):
    return Div(
        H3(func_info['name']),
        Code(func_info['signature']),
        P(func_info['doc'] or "No documentation"),
        render_parameters(func_info['params'])
    )

def render_api_page(api_data):
    return Div(
        H1(f"API Reference: {api_data['module']}"),
        *[render_function(f) for f in api_data['functions']]
    )
```

### Step 3: Integrate with App
```python
# app.py
from api_extractor import extract_module_api
from api_renderer import render_api_page

@app.get("/api/{module}")
def api_reference(module: str):
    api_data = extract_module_api(f"eidos.{module}")
    return layout(
        f"API: {module}",
        create_nav(),
        render_api_page(api_data)
    )
```

## Modules to Document

1. `eidos.tags` - All HTML components
2. `eidos.styles` - Style enums
3. `eidos.components.navigation` - NavBar component
4. `eidos.components.headers` - Header utilities
5. `eidos.plugins.markdown` - Markdown plugin

## Additional Features

1. **Type Hints Display**
   - Extract and display parameter types
   - Show return types

2. **Source Links**
   - Link to GitHub source
   - Show source code snippets

3. **Examples**
   - Extract from docstrings
   - Live component previews

4. **Search**
   - Index all API elements
   - Quick search functionality

## Example Output Structure

```
API Reference: eidos.tags

## Functions

### Button
`Button(*content, class_=None, **kwargs) -> Element`

Creates a button element with EidosUI styling.

Parameters:
- content: Button content
- class_: Additional CSS classes
- **kwargs: HTML attributes

Example:
Button("Click me", class_=styles.buttons.primary)

---

### H1
`H1(*content, cls=None, **kwargs) -> Element`
...
```

## Next Steps

1. Implement basic API extractor
2. Create renderer components
3. Add to documentation app
4. Style with EidosUI
5. Add search/filtering
6. Cache extracted data for performance