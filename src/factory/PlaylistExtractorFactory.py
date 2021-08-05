import os
from pathlib import Path
from PlaylistExtractor import PlaylistExtractor
from factory.TrackLoaderFactory import TrackLoaderFactory


class PlaylistExtractorFactory:
    def create_extractor(self, config, playlist, encoding="utf-8"):
        track_loader = TrackLoaderFactory().create_loader(config)
        return PlaylistExtractor(config.headers, playlist, track_loader, encoding)
