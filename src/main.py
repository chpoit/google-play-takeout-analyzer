from pathlib import Path

from loader.config_loader import load_config
from factory.PlaylistExtractorFactory import PlaylistExtractorFactory
from factory.TakeoutFactory import TakeoutFactory
from writer.PlaylistWriter import PlaylistWriter
from PlaylistExtractor import PlaylistExtractor

if __name__ == "__main__":
    playlists_to_extract = ["Thumbs up"]
    config = load_config()

    if not Path("out").exists() or True:
        takeout = TakeoutFactory().create_takeout(config)

        takeout.print()
        playlists = takeout.compress_playlists()

        PlaylistWriter(config).write_playlists(playlists)

    for playlist in playlists_to_extract:
        pe = PlaylistExtractorFactory().create_extractor(config, playlist)
        pe.move_playlist_data()
