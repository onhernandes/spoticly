def parse_playing_now_message(playback):
    """parse_playing_now_message

    :param playback: object
    :returns str
    """
    track = playback.get("item", {}).get("name", False)

    artist = playback.get("item", {}).get("artists", [])
    artist = map(lambda a: a.get("name", ""), artist)
    artist = ", ".join(list(artist))

    message = "Playing '%s' from '%s' now!" % (track, artist)
    if not track:
        message = "Could not get current track!"

    return message
