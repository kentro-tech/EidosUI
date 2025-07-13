# Contributing to EidosUI

Thank you for your interest in contributing to EidosUI! This guide will help you get started with development and ensure your contributions align with the project's standards.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Build Commands](#build-commands)
- [Import Guidelines](#import-guidelines)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Getting Started

### Prerequisites
- Python 3.10 or higher
- UV (recommended) or pip for dependency management
- Just command runner (optional but recommended)
- Git

### Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/kentro-tech/EidosUI.git
   cd EidosUI
   ```

## Development Setup

### Install Just (Recommended)
Just is a command runner that simplifies development tasks:
```bash
# macOS/Linux with Homebrew
brew install just

# Or download from https://github.com/casey/just/releases
```

### Quick Setup with Just
```bash
# Set up development environment
just dev
```

## Build Commands

We use `just` for common development tasks. Run `just` to see all available commands:

### Common Development Workflow
```bash
# Before making changes
just dev      # Set up environment (first time only)

# While developing
just check    # Run lint check, format check, and type check
just test     # Run tests
just docs     # Preview documentation

# Before committing
just clean    # Fix linting, format, and clean up generated files and caches
```

## Questions?

If you have questions or need help, please:
- Check existing issues on GitHub
- Create a new issue for bugs or feature requests
- Start a discussion for general questions

Thank you for contributing to EidosUI!