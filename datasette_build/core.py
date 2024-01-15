import pluggy
import importlib
from . import hookspecs

pm = pluggy.PluginManager("dsbuild")
pm.add_hookspecs(hookspecs)
pm.load_setuptools_entrypoints("dsbuild")

mod = importlib.import_module("datasette_build.default_formats")
pm.register(mod)


def get_formats():
    formats = []

    def register(format, extension=None):
        formats.append((format, extension))

    pm.hook.register_formats(register=register)
    return formats
