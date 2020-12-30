from loader.config_loader import load_config 
from factory.takeout_factory import TakeoutFactory 
from writer.playlist_writer import PlaylistWriter


if __name__ == "__main__":
    config = load_config()
    takeout = TakeoutFactory().create_takeout(config)

    takeout.print()
    playlists = takeout.compress_playlists()

    PlaylistWriter(config).write_playlists(playlists)