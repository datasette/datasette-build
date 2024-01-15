import click
from datasette_build.core import get_formats
import itertools
import pathlib
import sqlite_utils
from sqlite_utils.utils import TypeTracker


@click.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
)
@click.argument(
    "directory_path",
    type=click.Path(file_okay=False, dir_okay=True, allow_dash=False),
)
def cli(db_path, directory_path):
    """Build a directory full of files into a SQLite database"""
    formats = {}
    for format, ext in get_formats():
        formats[ext] = format

    db = sqlite_utils.Database(db_path)

    # Iterate through every file and directory in directory_path\
    path = pathlib.Path(directory_path)
    for child in path.iterdir():
        if child.is_file() and not child.stem.startswith("."):
            # It's a file, act based on its extension
            extension = child.suffix.lstrip(".")
            if extension in formats:
                rows = formats[extension].parse_file(child.open())
                first_row = next(rows)
                columns = list(first_row.keys())
                rows = itertools.chain([first_row], rows)
                pk = None
                if "id" in columns:
                    pk = "id"
                table_name = child.stem
                detect_types = getattr(formats[extension], "detect_types", False)
                tracker = None
                if detect_types:
                    tracker = TypeTracker()
                    rows = tracker.wrap(rows)
                db[table_name].insert_all(rows, pk=pk, replace=True)
                if tracker is not None:
                    db[table_name].transform(types=tracker.types)
                row_count = db[table_name].count
                click.echo(
                    "{} row{} in {}".format(
                        row_count, "" if row_count == 1 else "s", table_name
                    ),
                    err=True,
                )
        elif child.is_dir():
            click.echo("    is_dir: " + str(child), err=True)


if __name__ == "__main__":
    cli()
