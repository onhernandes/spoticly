"""
spoticly
Usage:
  spoticly auth
  spoticly next
  spoticly prev
  spoticly resume
  spoticly pause
  spoticly config
  spoticly -h | --help
  spoticly --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  spoticly config
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/onhernandes/spoticly
"""


from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import spoticly.commands

    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(spoticly.commands, k) and v:
            module = getattr(spoticly.commands, k)
            spoticly.commands = getmembers(module, isclass)
            command = [
                command[1] for command in spoticly.commands if command[0] != "Base"
            ][0]
            command = command(options)
            command.run()
