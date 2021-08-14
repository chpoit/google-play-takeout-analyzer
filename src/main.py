from pathlib import Path

from loader.config_loader import load_config
from factory.PlaylistExtractorFactory import PlaylistExtractorFactory
from factory.TakeoutFactory import TakeoutFactory
from writer.PlaylistWriter import PlaylistWriter
from PlaylistExtractor import PlaylistExtractor

if __name__ == "__main__":
    playlists_to_extract = []
    # playlists_to_extract = ["Thumbs up"]

    config = load_config()

    pw = PlaylistWriter(config)

    if not Path("out").exists():
        takeout = TakeoutFactory().create_takeout(config)

        takeout.print()
        playlists = takeout.compress_playlists(playlists_to_extract)

        pw.write_playlists(playlists)

    for playlist in playlists_to_extract:
        pe = PlaylistExtractorFactory().create_extractor(config, playlist)
        pw.write_missing_existing(pe)
