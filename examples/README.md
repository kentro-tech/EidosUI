# EidosUI Examples 🚀

This directory contains examples demonstrating EidosUI features and usage patterns.

## 🏃 Quick Start

### Running Examples with UV (Recommended)

From the project root:

```bash
# Install all dependencies including examples
uv sync --extra examples

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the basic example
cd examples
python basic_example.py
```

Then open http://localhost:8000 in your browser.

### Running Examples in a New Project

If you want to use these examples as a starting point for your own project:

```bash
# Create a new project
uv init my-eidos-project
cd my-eidos-project

# Add EidosUI with examples dependencies
uv add eidos-ui[examples]

# Copy an example file
cp /path/to/EidosUI/examples/basic_example.py ./app.py

# Run your app
uv run python app.py
```

## 📁 Available Examples

### `basic_example.py`
- **Purpose**: Minimal working example showing core EidosUI features
- **Features**:
  - Basic component usage (H1, Button, Card, Text)
  - Theme switching (light/dark)
  - Style mixing (defaults + custom Tailwind)
  - Static file serving
- **Best for**: Getting started, understanding the basics

## 🛠️ Development Tips

### Local Editable Install

When working on EidosUI itself:

```bash
# From project root
uv sync --all-extras  # Installs in editable mode automatically

# Run examples with your changes
cd examples
python basic_example.py
```

### Testing Changes

After modifying EidosUI components or styles:

1. No restart needed for CSS changes (just refresh browser)
2. Restart server for Python changes
3. Check both light and dark themes using the theme switcher

### Adding New Examples

When creating new examples:

1. Keep them simple and focused
2. Include comments explaining key concepts
3. Use meaningful variable names
4. Show both default styles and custom Tailwind
5. Test with both themes
6. Update this README

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors**:
```bash
# Make sure you're in the activated environment
source .venv/bin/activate

# Or run directly with uv
uv run python examples/basic_example.py
```

**Styles not loading**:
- Check that `serve_eidos_static(app)` is called
- Verify the server is running on the expected port
- Check browser console for 404 errors

**Theme switching not working**:
- Ensure JavaScript is enabled
- Check that the theme switcher button has `onclick="toggleTheme()"`
- Verify CSS files are loading correctly

### Getting Help

- Check the main README.md for API documentation
- Look at existing examples for patterns
- Create GitHub issues for bugs or feature requests 