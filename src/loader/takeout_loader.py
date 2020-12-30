import os
from takeout import Takeout


def load_takeout(takeout_location, encoding='utf-8'):

    scan = os.listdir(takeout_location)
    if scan[0] == 'Takeout':
        base_path = os.path.join(takeout_location, scan[0])
    else:
        base_path = takeout_location

    tracks_locations = os.path.join(base_path, 'Tracks')
    playlists_locations = os.path.join(base_path, 'Playlists')
    radio_stations_locations = os.path.join(base_path, 'Radio Stations')

    return Takeout(tracks_locations, playlists_locations, radio_stations_locations)

    
