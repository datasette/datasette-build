# datasette-build

[![PyPI](https://img.shields.io/pypi/v/datasette-build.svg)](https://pypi.org/project/datasette-build/)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-build?include_prereleases&label=changelog)](https://github.com/datasette/datasette-build/releases)
[![Tests](https://github.com/datasette/datasette-build/actions/workflows/test.yml/badge.svg)](https://github.com/datasette/datasette-build/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-build/blob/main/LICENSE)

Build a directory full of files into a SQLite database

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-build
```
## Usage

Usage instructions go here.

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
