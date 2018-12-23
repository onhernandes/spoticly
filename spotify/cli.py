"""
spotify-cli
Usage:
  spotify-cli auth
  spotify-cli next
  spotify-cli prev
  spotify-cli play <song|playlist> --playlist --artist --shuffle
  spotify-cli resume
  spotify-cli pause
  spotify-cli config
  spotify-cli -h | --help
  spotify-cli --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  spotify-cli config
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/onhernandes/spotify-cli
"""


from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import spotify.commands

    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(spotify.commands, k) and v:
            module = getattr(spotify.commands, k)
            spotify.commands = getmembers(module, isclass)
            command = [
                command[1] for command in spotify.commands if command[0] != "Base"
            ][0]
            command = command(options)
            command.run()
