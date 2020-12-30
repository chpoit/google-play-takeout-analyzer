import os
from takeout import Takeout
from loader.playlist_loader import PlaylistLoader


class TakeoutFactory():
    def create_takeout(self, config, encoding='utf-8'):
        takeout_location = config['takeout-path']
        headers = config['csv-headers']

        scan = os.listdir(takeout_location)
        if scan[0] == 'Takeout':
            base_path = os.path.join(
                takeout_location, scan[0], "Google Play Music")
        else:
            base_path = takeout_location

        tracks_locations = os.path.join(base_path, 'Tracks')
        playlists_locations = os.path.join(base_path, 'Playlists')
        radio_stations_locations = os.path.join(base_path, 'Radio Stations')

        return Takeout(PlaylistLoader(),
                       headers,
                       tracks_locations,
                       playlists_locations,
                       radio_stations_locations)
