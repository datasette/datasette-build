import click


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
    click.echo(f"{db_path}, {directory_path}")


if __name__ == "__main__":
    cli()
