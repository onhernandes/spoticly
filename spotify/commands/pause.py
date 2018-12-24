"""Next command."""
from .base import Base
from .. import spotify


class Pause(Base):
    """Pause playback"""

    def run(self):
        sp = spotify.get_spotipy()
        sp.pause_playback()
        print("Player paused!")
