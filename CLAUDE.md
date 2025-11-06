# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Table of Contents

- [Project Overview](#project-overview)
- [Development Commands](#development-commands)
  - [Linting and Formatting](#linting-and-formatting)
  - [Testing](#testing)
  - [Pre-commit Hooks](#pre-commit-hooks)
  - [Running the Application](#running-the-application)
- [Architecture](#architecture)
  - [Logging System](#logging-system)
  - [Testing Pattern](#testing-pattern)
- [CI/CD](#cicd)
- [Project Structure](#project-structure)
- [Important Notes](#important-notes)

## Project Overview

This is a Python project template designed for teaching and educational purposes. The codebase demonstrates production-ready logging patterns, decorator usage, and comprehensive testing practices.

## Development Commands

### Linting and Formatting

```bash
# Lint code (checks style and programming errors)
make lint
# Or directly: flake8 src/ test/

# Format code (auto-formats to Black style)
make format
# Or directly: black src/ test/

# Check formatting without modifying files
black --check src/ test/
```

Flake8 configuration in `.flake8`:
- Max line length: 88 (matches Black)
- Excludes: `__pycache__`, `.git`, `.venv`

### Testing

```bash
# Run all tests with detailed output
make test
# Or directly: pytest -v

# Run a specific test file
pytest test/test_tmp.py -s -v

# Run a specific test function
pytest test/test_tmp.py -k test_print_hi -s -v
```

### Pre-commit Hooks

The repository uses pre-commit hooks for Black and flake8. To set up:

```bash
pip install pre-commit
pre-commit install
```

This will automatically run Black and flake8 checks before each commit.

### Running the Application

```bash
python -m src.tmp
```

## Architecture

### Logging System

The project uses a custom logger utility (`src/utils/logger.py`) with the following characteristics:

- **RotatingFileHandler**: Logs rotate at 1MB with 5 backup files
- **Dual output**: Both file and console logging with different formats and levels
- **Default file location**: `logs/` directory (auto-created if missing)
- **Log naming**: `YYYY-MM-DD_{file_name}.log`

**Decorators:**
- `@func_wrapper(logger)`: Logs function start/end and handles exceptions
- `@sol_wrapper(logger)`: Logs entire solution/script execution (use once per script)

**Key pattern**: Functions store `__wrapped__` attribute to access undecorated versions, enabling test isolation by redecorating with test-specific loggers.

### Testing Pattern

Tests use `unittest` framework (pytest-compatible) with a critical logging isolation pattern:

```python
# In tests, redecorate functions with test logger to avoid log pollution
test_logger = create_logger(file_name="Test_File_Test", file_mode="w")
decorated_func = func_wrapper(test_logger)(original_func.__wrapped__)
```

This ensures test logs are separate from production logs.

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on push/PR to main:
1. Lint with flake8
2. Format check with Black
3. Run all tests with pytest

Additional workflows: `codeql.yml`, `security.yml` for security scanning.

## Project Structure

```
src/
  utils/
    logger.py         # Custom logging utilities and decorators
  tmp.py              # Example script demonstrating logging patterns
test/
  test_tmp.py         # Tests with logger isolation pattern
logs/                 # Auto-generated log files (gitignored)
```

## Important Notes

- All code files should start with 2-line ABOUTME comments describing the file's purpose
- The project uses Python 3.12
- Requirements are split: `requirements.txt` (production), `requirements-dev.txt` (development tools)
- Tests MUST use the decorator unwrapping pattern (`func.__wrapped__`) to maintain log isolation