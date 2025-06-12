# Name of Your Project

An introduction paragraph must contain a brief fescription of the project. If there are acronymns, create a section with a [table](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables) for this so they can be spelled out correctly.

## Acronymns

| Acronymn | spelled out  | description as needed |
| :------: | :----------- | --------------------: |
|   `CC`   | Content Cell |  a place in the table |

Your introduction should also include:

- 1-1 sentences describing the problem to solve
- audience / end user the solution is for
- how to run

## Requirements

What are the requirements for success of thsi repo? What are your milestones, nice to haves, etc?

# Getting Started

These instructions will provide a copy of the project & get you running on your local machine for development and testing purposes.

See [deployment](#deployment) section on how to deploy a project as a live system.

Note that there are GitHub actions to support improved static code reviews, such as `codeql` and security.

## Pre-requisites

What you need in order to run this project & where to go / how to install them.

Please be sure to leverage the `requirements.txt` file.

# How To For ...

## Installing

Step by step explanation on how to get a development ENV running.

This was originally written in INSERT_VERSION of python.

## Linting

### Manual

If you are able to use Make, you can run eah command independently or combine them:

```
make lint && make format && make test
```

`make lint` checks code for style & programming errors ... If this is not an option, you can run:

```python
flake8 src/ test/
```

This will tell you what the issues are. More on configuring flake8 [here](https://flake8.pycqa.org/en/latest/user/configuration.html).

![Example of running flake8](/IMGs/Examples/example-flake8.png)

To check if your code is already formatted (without making changes), run:

```python
black --check src/ test/
```

`make format` automatically formats your code to follow Black style guide. If that is not available, you can run:

```python
black src/ test/
```

![Example of running black](/IMGs/Examples/example-black.png)

**TO NOTE:**

- Black is an uncompromising Python code formatter.
- It reformats your code to be consistent and readable.
- It is opinionated: you don’t configure much, just run it and it formats your code.
- It helps avoid style debates and keeps codebases consistent.

`make test` runs all test and shows detailed output.

### Pre Commit Check

A `.pre-commit-config.yaml` file has been created in project root. (Learn more about this [here](https://pre-commit.com/).) This will enable you to use pre-commit for black and flake8 checks before each commit, but it will not automatically update your code—only check and block commits if issues are found.

To set it up:

1. Add `pre-commit` to your requirements file (DEV not PROD)

2. Ensure the YAML file is in the right place at the project root

3. Run the following in your expected virtual environment:

    ```
    pip install pre-commit
    pre-commit install
    ```

This will set up the hooks for your local git repository.

## Testing

### Locally

To run a test file, from the main folder run a line similar to the following:

```python
pytest test/test_tmp.py -s -v
```

If you would like to run a specific test, follow a syntax similar to:

```python
pytest test/test_tmp.py -k test_print_hi -s -v
```

### GitHub Actions

The following section is care of GitHub Copilot.

The CI file (.github/workflows/ci.yml) is a GitHub Actions workflow that automates code quality checks and testing for your repository. Here’s what it does:

1. Triggers:
   - Runs on every push or pull request to the main branch.
2. Environment:
   - Uses the latest Ubuntu runner provided by GitHub.
3. Steps:
   - **Checkout code:** Downloads your repository code to the runner.
   - **Set up Python:** Installs Python 3.12.
   - **Install dependencies:**
     - Upgrades pip.
     - Installs all packages listed in requirements.txt.
     - Installs `flake8`, `black`, and `pytest` (in case they’re not in requirements.txt).
   - **Lint:** Runs make lint to check your code for style and programming errors using flake8.
   - **Format Check:** Runs `black --check src/ test/` to ensure your code is formatted according to Black’s standards (but does not reformat).
   - **Test:** Runs make test to execute all your tests and show detailed output.

**Summary:**
This workflow ensures that every code change is automatically checked for style, formatting, and correctness before being merged, helping maintain code quality and consistency in your project.

## Deployment

Information on how to deploy to a live system.

## Usage

How to use this solution.

If additional documentation is stored elsewhere, it will be noted here.

This template repo would say that in the main folder of this project in a CLI, run the following:

```python
python -m src.tmp.py
```

# Support Information

## Support Contacts

The current owner of this repo is an individual. If you would like to discuss something outside of submitting an issue, please see the contact us section from [here](https://resume.prosperousheart.com/).

## Health Monitoring

Where applicable, document how the health of teh application is being monitored & how operators can be made aware of new issues.

# Contributing

See [contributing file](contributing.md).

## Authors

Currently only @prosperousheart.

## License

See [license](license.md) file.

## Acknowledgements

Thank you to anyone who helps contribute to this project!
