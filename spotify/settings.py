import yaml
import os

config_dir = os.path.join(os.path.expanduser("~"), ".config/spotify-cli/")
config_filepath = os.path.join(config_dir, "settings.yaml")


def ensure_config_file():
    default_settings = {
        "SPOTIPY_CLIENT_ID": "",
        "SPOTIPY_CLIENT_SECRET": "",
        "SPOTIPY_REDIRECT_URI": "",
        "SPOTIPY_SCOPES": [
            "user-read-playback-state",
            "user-read-currently-playing",
            "user-modify-playback-state",
            "user-read-private",
            "streaming",
        ],
        "SPOTIPY_TOKEN": "",
        "SPOTIPY_USERNAME": "",
    }
    if not os.path.isdir(config_dir):
        os.mkdir(config_dir)

    if not os.path.exists(config_filepath):
        with open(config_filepath, "w") as outfile:
            return yaml.dump(default_settings, outfile, default_flow_style=False)


ensure_config_file()


def get_config():
    with open(config_filepath, "r") as conf:
        return yaml.load(conf)


def get(k):
    y = get_config()
    return y.get(k)


def set(data):
    y = get_config()
    for k, v in y.items():
        if data.get(k, None) is None:
            data[k] = v
    with open(config_filepath, "w") as outfile:
        return yaml.dump(data, outfile, default_flow_style=False)


def get_all():
    y = get_config()
    return y


def ensure_all():
    y = get_config()
    """Ensure all values are set
    :returns: True/False

    """
    keys = [
        "SPOTIPY_CLIENT_ID",
        "SPOTIPY_CLIENT_SECRET",
        "SPOTIPY_REDIRECT_URI",
        "SPOTIPY_USERNAME",
    ]
    values = [y.get(k, False) for k in keys]
    return all(values)
