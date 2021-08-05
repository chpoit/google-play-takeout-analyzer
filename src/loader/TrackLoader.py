from pathlib import Path


class TrackLoader:
    def __init__(self, tracks_dir):
        self.tracks_dir = tracks_dir

        self.load_tracks()

    def load_tracks(self):
        self.tracks_dir
