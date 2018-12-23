import sys


def get_spotipy(arg1):
    from . import settings

    if not settings.ensure_all():
        print("You must set your Spotify's app config!")
        print("Run spotify-cli config")
        sys.exit()
