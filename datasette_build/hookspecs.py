from pluggy import HookimplMarker
from pluggy import HookspecMarker

hookspec = HookspecMarker("dsbuild")
hookimpl = HookimplMarker("dsbuild")


@hookspec
def register_formats(register):
    "Register classes to handle different file formats"
