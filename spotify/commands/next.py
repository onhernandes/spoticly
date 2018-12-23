"""Next command."""
from .base import Base
from .. import settings
from .. import utils

import spotipy


class Next(Base):
    """Authenticate user"""

    def run(self):
        print(utils.get_spotipy_token())
        sp = spotipy.Spotify(auth=utils.get_spotipy_token())
        sp.next_track()
        current = sp.current_playback()
        current_track = current.get("item", {}).get("name", False)

        current_artist = current.get("item", {}).get("artists", [])
        current_artist = map(lambda a: a.get("name", ""), current_artist)
        current_artist = ", ".join(list(current_artist))

        message = "Playing '%s' from '%s' now!" % (current_track, current_artist)
        if not current_track:
            message = "Could not get current track!"
        print(message)
