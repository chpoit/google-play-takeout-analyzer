
class Takeout:
    def __init__(self, tracks_locations, playlists_locations, radio_stations_locations):
        self.tracks_locations = tracks_locations
        self.playlists_locations = playlists_locations
        self.radio_stations_locations = radio_stations_locations

    def print(self):
        print(f"Tracks: {self.tracks_locations}")
        print(f"Playlists: {self.playlists_locations}")
        print(f"Radio Stations: {self.radio_stations_locations}")
    