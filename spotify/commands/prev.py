"""Next command."""
from .base import Base
from .. import spotify
from ..utils import parse_playing_now_message


class Previous(Base):
    """Play previous track"""

    def run(self):
        sp = spotify.get_spotipy()
        sp.previous_track()
        playback = sp.current_playback()
        print(parse_playing_now_message(playback))
