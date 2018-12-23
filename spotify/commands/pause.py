"""Next command."""
from .base import Base
from .. import settings
from .. import utils

import spotipy


class Pause(Base):
    """Authenticate user"""

    def run(self):
        sp = spotipy.Spotify(auth=utils.get_spotipy_token())
        sp.pause_playback()
        print("Player paused!")
