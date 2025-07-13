# Default recipe to show available commands
default:
    @just --list

# Set up development environment (creates venv and installs)
dev:
    uv venv
    @echo "Virtual environment created. Activate with:"
    @echo "  source .venv/bin/activate  # Linux/macOS"
    @echo "  .venv\\Scripts\\activate     # Windows"
    uv pip install -e ".[dev]"

# Run all quality checks (lint, format, typecheck)
check: 
    ruff check eidos/ tests/ docs/
    ruff format --check eidos/ tests/ docs/
    mypy eidos/

# Fix linting, format, and clean up generated files and caches
clean:
    ruff check --fix eidos/ tests/ docs/
    ruff format eidos/ tests/ docs/
    rm -rf dist/ build/ *.egg-info
    rm -rf htmlcov/ .coverage .pytest_cache/ .mypy_cache/ .ruff_cache/
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Run all tests
test:
    python -m pytest tests/ -v

# Build distribution packages
build:
    rm -rf dist/
    python -m build

# Build and serve documentation locally
docs:
    cd docs && fastapi dev

# Create a new release (version should be passed as argument)
release version:
    @echo "Creating release {{version}}..."
    # Update version in pyproject.toml
    sed -i.bak 's/version = ".*"/version = "{{version}}"/' pyproject.toml && rm pyproject.toml.bak
    # Update version in __init__.py
    sed -i.bak 's/__version__ = ".*"/__version__ = "{{version}}"/' eidos/__init__.py && rm eidos/__init__.py.bak
    # Commit version bump
    git add pyproject.toml eidos/__init__.py
    git commit -m "Bump version to {{version}}"
    # Create tag
    git tag -a v{{version}} -m "Release v{{version}}"
    @echo "Release v{{version}} created. Push with:"
    @echo "  git push origin main"
    @echo "  git push origin v{{version}}"
