"""Next command."""
from .base import Base
from .. import spotify
from ..utils import parse_playing_now_message


class Next(Base):
    """Play next track"""

    def run(self):
        sp = spotify.get_spotipy()
        sp.next_track()
        playback = sp.current_playback()
        print(parse_playing_now_message(playback))
