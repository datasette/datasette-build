# datasette-build

[![PyPI](https://img.shields.io/pypi/v/datasette-build.svg)](https://pypi.org/project/datasette-build/)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-build?include_prereleases&label=changelog)](https://github.com/datasette/datasette-build/releases)
[![Tests](https://github.com/datasette/datasette-build/actions/workflows/test.yml/badge.svg)](https://github.com/datasette/datasette-build/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-build/blob/main/LICENSE)

Build a directory full of files into a SQLite database

## Installation

Install this tool using `pip` or `pipx`:
```bash
pipx install datasette-build
```
This will provide the `datasette-build` CLI application.

You can also install it as a Datasette plugin. First [install Datasette](https://docs.datasette.io/en/stable/installation.html), then run:
```bash
datasette install datasette-build
```
This will provide a `datasette build ...` command that works the same as the `datasette-build` CLI application.

Or you can install it as a plugin for [sqlite-utils](https://sqlite-utils.datasette.io/). With that installed, run this:
```bash
sqlite-utils install datasette-build
```
Now you can access the tool as `sqlite-utils build ...`

## Usage



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-build
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
