import sys
import requests
from . import settings

spotify_base = "https://api.spotify.com/v1"


def get_spotipy_token():
    import spotipy.util as util

    params = get_spotify_auth_params()
    return util.prompt_for_user_token(**params)


def get_headers(token):
    return {"Authorization": "Bearer %s" % (token)}


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


def previous_track(token):
    url = "%s/me/player/previous" % (spotify_base)
    r = requests.post(url, headers=get_headers(token))

    return r.status_code == 204


def next_track(token):
    url = "%s/me/player/next" % (spotify_base)
    r = requests.post(url, headers=get_headers(token))

    return r.status_code == 204


def get_current_playback(token):
    url = "%s/me/player" % (spotify_base)
    r = requests.get(url, headers=get_headers(token))

    return r.json()


def pause_playback(token):
    url = "%s/me/player/pause" % (spotify_base)
    r = requests.put(url, headers=get_headers(token))

    return r.status_code == 204


def resume_playback(token):
    url = "%s/me/player/play" % (spotify_base)
    r = requests.put(url, headers=get_headers(token))

    return r.status_code == 204
