Also link to Issues where possible.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

## [Unreleased]

TBD

## [1.3.0] - 2025-06-12

### Added

- logging utility script
- README to utility folder to show original code (removing from logger file)

### Updated

- added logs folder to gitignore
- added `__init__.py` for utils folder
- added logging and docstrings to test file
- add logging to main file
- added log file size and number limitation through filehandler rotation
- instead of passing the logger between functions, brought it out
- to make testing work, moved logger into the decorator argument & updated logging utility

## [1.2.0] - 2025-06-11

### Added

- CONTRIBUTING file
- codeql YAML worklflow file
- security YAML worklflow file
- requiements file (for DEV and PROD)
- folder structure for future code, including src & test folders & placeholder python files
- images of examples when running linters
- flake8 config file
- make file
- pre-commit file

### Updated

- README to indicate the workflows added
- README to include info on requirements file & running code/tests
- README to include section on linting
- src and test code files to give example of working test with code
- README on flake8 config
- README on pre-commit setup

## [1.1.0] - 2024-05-10

### Added

- basic repo setup with MIT license and python .gitignore file
- README template
- code of conduct
- PR template
- issue templates (bug, feature, documentation)
