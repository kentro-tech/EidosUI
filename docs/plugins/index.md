# Plugins

Optional extensions for EidosUI.

## Available Plugins

### [Markdown](/plugins/markdown)

Complete guide to markdown in EidosUI - from basic usage to creating custom extensions.

```bash
pip install "eidosui[markdown]"
```

## Creating Plugins

Plugins extend EidosUI without bloating core.

### Structure

```python
# eidos/plugins/myplugin/__init__.py
from .components import MyComponent
from .renderer import MyRenderer

__all__ = ["MyComponent", "MyRenderer"]
```

### Packaging

Add to `pyproject.toml`:

```toml
[project.optional-dependencies]
myplugin = ["dependency1", "dependency2"]
```

### Guidelines

- Use EidosUI CSS variables
- Provide CSS component  
- Include documentation
- Add type hints