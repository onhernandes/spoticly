"""Next command."""
from .base import Base
from .. import spotify


class Resume(Base):
    """Authenticate user"""

    def run(self):
        sp = spotify.get_spotipy()
        sp.start_playback()
        print("Player resumed!")
