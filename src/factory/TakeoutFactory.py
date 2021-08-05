import os
from pathlib import Path
from Takeout import Takeout
from loader.PlaylistLoader import PlaylistLoader


class TakeoutFactory:
    def create_takeout(self, config, encoding="utf-8"):
        takeout_location = config["takeout-path"]
        headers = config["csv-headers"]

        scan = os.listdir(takeout_location)
        if scan[0] == "Takeout":
            base_path = Path(takeout_location, scan[0], "Google Play Music")
        elif "Google Play Music" in scan:
            base_path = Path(takeout_location, "Google Play Music")
        else:
            base_path = takeout_location

        tracks_locations = Path(base_path, "Tracks")
        playlists_locations = Path(base_path, "Playlists")
        radio_stations_locations = Path(base_path, "Radio Stations")

        return Takeout(
            PlaylistLoader(),
            headers,
            tracks_locations,
            playlists_locations,
            radio_stations_locations,
        )
