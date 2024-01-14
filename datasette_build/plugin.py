from datasette import hookimpl


@hookimpl
def register_commands(cli):
    from .cli import cli as build_cli

    cli.add_command(build_cli, name="build")
