# Contributing to EidosUI

Thank you for your interest in contributing to EidosUI! This guide will help you get started with development and ensure your contributions align with the project's standards.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Import Guidelines](#import-guidelines)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Getting Started

### Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/EidosUI.git
   cd EidosUI
   ```

## Development Setup

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## Testing

### Import Testing
Always test that your additions work with all import patterns:
```python
# Test 1: Star import
from eidos import *
assert MyComponent is not None

# Test 2: Direct import
from eidos import MyComponent
assert MyComponent is not None

# Test 3: Submodule import
from eidos.components import MyComponent
assert MyComponent is not None
```

(Testing guidelines will be added when test infrastructure is set up)

## Submitting Changes

## Questions?

If you have questions or need help, please:
- Check existing issues on GitHub
- Create a new issue for bugs or feature requests
- Start a discussion for general questions

Thank you for contributing to EidosUI!