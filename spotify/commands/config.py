"""Config command."""
from __future__ import print_function, unicode_literals
from json import dumps
from .base import Base
from .. import settings

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2


class Config(Base):
    """Set spotify config"""

    def init_config(self):
        config_questions = [
            {
                "type": "input",
                "name": "SPOTIPY_USERNAME",
                "message": "Your Spotify's username",
            },
            {"type": "input", "name": "SPOTIPY_CLIENT_ID", "message": "Your client ID"},
            {
                "type": "input",
                "name": "SPOTIPY_CLIENT_SECRET",
                "message": "Your client secret",
            },
            {
                "type": "input",
                "name": "SPOTIPY_REDIRECT_URI",
                "message": "Your redirect URL",
            },
        ]
        answers = prompt(config_questions, style=custom_style_2)
        settings.set(answers)
        print("You are all set!")

    def config(self):
        config_questions = [
            {
                "type": "list",
                "name": "what_change",
                "message": "What you wanna change?",
                "choices": [
                    "Client ID",
                    "Client Secret",
                    "Redirect URI",
                    "Username",
                    "Nah, nothing",
                ],
            },
            {
                "type": "input",
                "name": "new_value",
                "message": "So, whats new?",
                "when": lambda answers: answers.get("what_change") != "Nah, nothing",
            },
        ]
        answers = prompt(config_questions, style=custom_style_2)
        if not answers.get("new_value", False):
            return
        empty_dict = {}
        value = answers.get("new_value")
        key = answers.get("what_change")
        if key == "Client ID":
            key = "SPOTIPY_CLIENT_ID"
        if key == "Client Secret":
            key = "SPOTIPY_CLIENT_SECRET"
        if key == "Redirect URI":
            key = "SPOTIPY_REDIRECT_URI"
        if key == "Username":
            key = "SPOTIPY_USERNAME"
        empty_dict[key] = value
        settings.set(empty_dict)
        print("Updated!")

    def run(self):
        if not all(list(settings.get_all().values())):
            return self.init_config()

        return self.config()
