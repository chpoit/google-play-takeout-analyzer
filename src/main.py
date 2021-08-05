from loader.config_loader import load_config
from factory.TakeoutFactory import TakeoutFactory
from writer.PlaylistWriter import PlaylistWriter
from PlaylistExtractor import PlaylistExtractor
from PlaylistExtractor import PlaylistExtractor

if __name__ == "__main__":
    playlists_to_extract = ["Thumbs Up"]

    config = load_config()
    takeout = TakeoutFactory().create_takeout(config)

    takeout.print()
    playlists = takeout.compress_playlists(playlists_to_extract)

    PlaylistWriter(config).write_playlists(playlists)

    for playlist in playlists_to_extract:
        PlaylistExtractor(playlist).move_playlist_data()
