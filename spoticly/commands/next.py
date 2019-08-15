"""Next command."""
from .base import Base
from .. import spotify
from ..utils import parse_playing_now_message
from time import sleep


class Next(Base):
    """Play next track"""

    def run(self):
        token = spotify.get_spotipy_token()
        spotify.next_track(token)
        sleep(0.3)
        playback = spotify.get_current_playback(token)
        print(parse_playing_now_message(playback))
