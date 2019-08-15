"""Auth command."""
from .base import Base
from .. import settings, spotify

import spotipy


class Auth(Base):
    """Authenticate user"""

    def run(self):
        token = spotify.get_spotipy_token()
        settings.set({"SPOTIPY_TOKEN": token})
        sp = spotipy.Spotify(auth=token)
        me = sp.me()
        print("User %s authenticated!" % (me.get("display_name")))
