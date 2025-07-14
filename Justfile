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

# Build distribution packages
build:
    rm -rf dist/
    python -m build

# Build and serve documentation locally
docs:
    cd docs && fastapi dev

release:
    just clean
    python -m build
    twine upload --skip-existing dist/*
