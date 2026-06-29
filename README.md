CI/CD Pipeline Demo (Calculator)

Simple Python project demonstrating a CI/CD pipeline using GitHub Actions.

Purpose

This project shows how CI works by automatically running linting and tests on every push.

It also includes an optional autofix mode for Ruff controlled by the commit message.

What happens on push
Ruff checks code quality
Pytest runs unit tests
Results are shown in GitHub Actions

If anything fails, the pipeline stops.

Autofix feature

If a commit message contains the word:

autofix

Ruff will run in fix mode:

ruff check . --fix

Otherwise, Ruff only checks the code without modifying it.

Example:

git commit -m "autofix: fix lint issues"

This allows developers to explicitly request automatic code fixes through the CI pipeline.

Project structure
calculator/
├── calculator.py
├── test_calculator.py
└── .github/workflows/ci.yml
Example workflow
name: CI

on: push

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest ruff

      - run: ruff check .

      - run: pytest
Run locally
pip install pytest ruff
ruff check .
pytest
Tools

Python
Pytest
Ruff
GitHub Actions
