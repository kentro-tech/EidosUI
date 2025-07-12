# EidosUI Documentation

This is the official documentation for EidosUI, built as a runnable web application using EidosUI itself.

## Running the Documentation

### Prerequisites

Make sure you have EidosUI installed:

```bash
pip install "eidosui[markdown]"
```

### Start the Documentation Server

From the docs directory:

```bash
python app.py
```

Or from the project root:

```bash
python docs/app.py
```

The documentation will be available at `http://localhost:8000`

## Features

- **Live Examples**: See EidosUI components in action
- **Interactive Demos**: Try out different themes and styles
- **Comprehensive Guides**: From getting started to advanced customization
- **About Section**: Learn about the project's influences and philosophy

## Documentation Structure

- `/` - Introduction and overview
- `/getting-started` - Installation and quick start guide
- `/components` - Complete component reference
- `/styling` - CSS system and theming
- `/philosophy` - Design principles and architecture
- `/plugins` - Plugin system overview
- `/plugins/markdown` - Markdown plugin documentation
- `/plugins/markdown-extensions` - Creating custom markdown extensions
- `/about` - Project history, influences, and comparison with MonsterUI
- `/demo` - Live component demonstrations

## Development

To add new documentation pages:

1. Create a new markdown file in the appropriate directory
2. Add a route handler in `app.py`
3. Update the sidebar navigation in the `layout()` function

## Theme Toggle

Click the moon/sun icon in the navigation bar to switch between light and dark themes.