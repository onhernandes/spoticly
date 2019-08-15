"""Next command."""
from .base import Base
from .. import spotify


class Pause(Base):
    """Pause playback"""

    def run(self):
        token = spotify.get_spotipy_token()
        spotify.pause_playback(token)
        print("Player paused!")
