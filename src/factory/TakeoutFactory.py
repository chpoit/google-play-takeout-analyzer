import os
from pathlib import Path
from Takeout import Takeout
from loader.PlaylistLoader import PlaylistLoader


class TakeoutFactory:
    def create_takeout(self, config, encoding="utf-8"):
        return Takeout(
            PlaylistLoader(),
            config.headers,
            config.tracks_location,
            config.playlists_location,
            config.radio_stations_location,
        )
