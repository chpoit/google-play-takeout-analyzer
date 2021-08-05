import os
import csv
from pathlib import Path

from loader.PlaylistLoader import PlaylistLoader


class Takeout:
    def __init__(
        self,
        playlist_loader: PlaylistLoader,
        csv_headers,
        tracks_locations,
        playlists_locations,
        radio_stations_locations,
    ):
        self.playlist_loader = playlist_loader
        self.csv_headers = csv_headers
        self.tracks_locations = tracks_locations
        self.playlists_locations = playlists_locations
        self.radio_stations_locations = radio_stations_locations

    def print(self):
        print(f"Tracks: {self.tracks_locations}")
        print(f"Playlists: {self.playlists_locations}")
        print(f"Radio Stations: {self.radio_stations_locations}")

    def compress_playlists(self, playlists=None):
        if playlists is None:
            pass
        elif type(playlists) is str:
            playlists = [playlists]
        elif len(playlists) == 0:
            playlists = None

        track_list = {}
        for name in os.scandir(self.playlists_locations):
            if playlists is None or name in playlists:
                playlist_path = Path(self.playlists_locations, name)
                track_list[name.name] = self.playlist_loader.load_playlist_tracks(
                    playlist_path
                )

        # print(track_list)
        return track_list
