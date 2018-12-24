import sys
from . import settings


def get_spotipy_token():
    import spotipy.util as util

    params = get_spotify_auth_params()
    return util.prompt_for_user_token(**params)


def get_spotify_auth_params():
    return {
        "client_id": settings.get("SPOTIPY_CLIENT_ID"),
        "client_secret": settings.get("SPOTIPY_CLIENT_SECRET"),
        "redirect_uri": settings.get("SPOTIPY_REDIRECT_URI"),
        "username": settings.get("SPOTIPY_USERNAME"),
        "scope": " ".join(list(settings.get("SPOTIPY_SCOPES"))),
    }


def ensure_settings():
    """Ensure user set needed API config
    :returns: None

    """
    if not settings.ensure_all():
        print("You must set your Spotify's app config!")
        print("Run spotify-cli config")
        sys.exit()


def get_spotipy():
    ensure_settings()
    import spotipy
    token = get_spotipy_token()
    return spotipy.Spotify(auth=token)
