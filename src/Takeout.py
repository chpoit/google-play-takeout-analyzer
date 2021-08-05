import os
import csv
from pathlib import Path

from loader.PlaylistLoader import PlaylistLoader


class Takeout:
    def __init__(
        self,
        playlist_loader: PlaylistLoader,
        csv_headers,
        tracks_location,
        playlists_location,
        radio_stations_location,
    ):
        self.playlist_loader = playlist_loader
        self.csv_headers = csv_headers
        self.tracks_location = tracks_location
        self.playlists_location = playlists_location
        self.radio_stations_location = radio_stations_location

    def print(self):
        print(f"Tracks: {self.tracks_location}")
        print(f"Playlists: {self.playlists_location}")
        print(f"Radio Stations: {self.radio_stations_location}")

    def compress_playlists(self, playlists=None):
        if playlists is None:
            pass
        elif type(playlists) is str:
            playlists = [playlists]
        elif len(playlists) == 0:
            playlists = None


        track_list = {}
        for file_name in os.scandir(self.playlists_location):
            if playlists is None or file_name.name in playlists:
                playlist_path = Path(self.playlists_location, file_name)
                track_list[file_name.name] = self.playlist_loader.load_playlist_tracks(
                    playlist_path
                )

        return track_list
