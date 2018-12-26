"""Next command."""
from .base import Base
from .. import spotify
from ..utils import parse_playing_now_message


class Next(Base):
    """Play next track"""

    def run(self):
        token = spotify.get_spotipy_token()
        spotify.next_track(token)
        playback = spotify.get_current_playback(token)
        print(parse_playing_now_message(playback))
