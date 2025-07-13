# Plugins

Optional extensions for EidosUI.

## Available Plugins

### [Markdown](markdown)

Theme-aware markdown rendering.

```bash
pip install "eidosui[markdown]"
```

Features:
- GitHub Flavored Markdown
- GitHub-style alerts
- Theme integration
- Custom extensions

### [Markdown Extension Guide](markdown-extension-guide)

Create custom markdown extensions.

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