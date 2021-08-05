import json
import os
from pathlib import Path

HOME = str(Path.home())


class Config:
    def __init__(self, config_json):
        self.takeout_location = Path(config_json["takeout-path"])
        self.headers = config_json["csv-headers"]

        scan = os.listdir(self.takeout_location)
        if scan[0] == "Takeout":
            base_path = Path(self.takeout_location, scan[0], "Google Play Music")
        elif "Google Play Music" in scan:
            base_path = Path(self.takeout_location, "Google Play Music")
        else:
            base_path = self.takeout_location

        self.base_path = base_path

    @property
    def takeout_path(self):
        return self.takeout_location

    @property
    def tracks_location(self):
        return Path(self.base_path, "Tracks")

    @property
    def playlists_location(self):
        return Path(self.base_path, "Playlists")

    @property
    def radio_stations_location(self):
        return Path(self.base_path, "Radio Stations")


def load_config(config_path="", encoding="utf-8"):

    if not config_path:
        config_path = "./config.json"

    config_path = config_path.replace("~", HOME)

    with open(config_path, encoding=encoding) as f:
        config = json.load(f)

    config["takeout-path"] = config["takeout-path"].replace("~", HOME)

    return Config(config)
