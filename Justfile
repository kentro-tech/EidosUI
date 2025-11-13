# Default recipe to show available commands
default:
    @just --list

# Run linting
lint:
    ruff check eidos/ tests/ docs/

# Check code formatting (without modifying)
format-check:
    ruff format --check eidos/ tests/ docs/

# Format code
format:
    ruff format eidos/ tests/ docs/

# Run type checking
typecheck:
    mypy eidos/

# Run all quality checks (lint, format, typecheck)
check: lint format-check typecheck

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

# Run tests with coverage
test-cov:
    python -m pytest tests/ -v --cov=eidos --cov-report=xml --cov-report=html --cov-report=term-missing

# Build and serve documentation locally
docs:
    uv pip install -e ".[markdown]" && cd docs && uv run fastapi dev app.py

# Release to PyPI and deploy docs
release:
    just clean
    rm -rf dist/
    uv build
    uv publish
    railway up -c
