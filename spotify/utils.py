def get_spotipy_token():
    from . import settings
    import spotipy
    import spotipy.util as util

    scopes = "user-read-playback-state user-read-currently-playing user-modify-playback-state user-read-private streaming"
    username = settings.get("SPOTIPY_USERNAME")
    client_id = settings.get("SPOTIPY_CLIENT_ID")
    client_secret = settings.get("SPOTIPY_CLIENT_SECRET")
    redirect_uri = settings.get("SPOTIPY_REDIRECT_URI")
    return util.prompt_for_user_token(username, 
            scopes, client_id=client_id, 
            client_secret=client_secret, redirect_uri=redirect_uri)
