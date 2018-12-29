"""Next command."""
from .base import Base
from .. import spotify


class Resume(Base):
    """Authenticate user"""

    def run(self):
        token = spotify.get_spotipy_token()
        spotify.resume_playback(token)
        print("Player resumed!")
