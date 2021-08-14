from pathlib import Path
import os

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

    out_p = Path("out")
    print("a")
    if not out_p.exists() or len(os.listdir(out_p)) == 0:
        takeout = TakeoutFactory().create_takeout(config)

        takeout.print()
        playlists = takeout.compress_playlists(playlists_to_extract)

        pw.write_playlists(playlists)
        if len(playlists_to_extract) == 0:
            playlists_to_extract = [key for key in playlists]

    for playlist in playlists_to_extract:
        pe = PlaylistExtractorFactory().create_extractor(config, playlist)
        pw.write_missing_existing(pe)
