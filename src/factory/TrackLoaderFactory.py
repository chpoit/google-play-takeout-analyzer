import os
from pathlib import Path
from loader.TrackLoader import TrackLoader

class TrackLoaderFactory:
    def create_loader(self, config):
        return TrackLoader(config.tracks_location)
