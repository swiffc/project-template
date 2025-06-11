# Contributing to Cursor Development System

Thank you for your interest in contributing to the Cursor Development System! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Development Setup

1. Fork the repository
2. Clone your fork:

   ```bash
   git clone https://github.com/your-username/cursor-dev-system.git
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   .venv\Scripts\activate     # Windows
   ```

4. Install development dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a new branch for your feature/fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Run tests:

   ```bash
   pytest
   ```

4. Run linting:

   ```bash
   flake8
   mypy
   black .
   isort .
   ```

5. Commit your changes:

   ```bash
   git commit -m "feat: add new feature"
   ```

6. Push to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request

## Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

## Pull Request Process

1. Update documentation for any new features
2. Add tests for new functionality
3. Ensure all tests pass
4. Update the changelog
5. Request review from maintainers

## Testing

- Write unit tests for new features
- Ensure existing tests pass
- Add integration tests for complex features
- Test on multiple Python versions

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions/classes
- Update API documentation
- Add examples for new features

## Style Guide

- Follow PEP 8
- Use type hints
- Write descriptive docstrings
- Keep functions focused and small
- Use meaningful variable names

## Release Process

1. Update version in `pyproject.toml`
2. Update changelog
3. Create release tag
4. Build and publish to PyPI

## Questions?

Feel free to open an issue for any questions or concerns.
