import os
from pathlib import Path
import regex as re


class TrackLoader:
    def __init__(self, tracks_dir):
        self.tracks_dir = tracks_dir

        self.load_tracks()

    def load_tracks(self):
        self.tracks = set()
        self.tracks_mp3 = set()
        for f in os.scandir(self.tracks_dir):
            name = f.name
            set_to_use = self.tracks_mp3 if name.endswith(".mp3") else self.tracks

            name = self.remove_ext(name)
            name = self.clean_name(name)

            set_to_use.add(name.lower())

    def remove_ext(self, name):
        # only exts in my tracks dir, can't only rely on split ext because of "feat." and others
        # runs multiple time for weird .mp3.csv or .mp3.mp3 cases
        while name.endswith(".csv") or name.endswith(".mp3"):
            name, ext = os.path.splitext(name)
        return name

    def clean_name(self, name):
        name = name.replace('"', "")
        name = re.sub(r"\(.*\)", "", name)
        name = re.sub(r"\[.*\]", "", name)
        # name = name.split(",")[0]
        new_name = name
        try:
            while not new_name[0].isalnum():
                new_name = new_name[1:]
            name = new_name
        except:
            pass
        return name.strip()

    def contains(self, track_name):
        """
        Returns if track exists and if it's an mp3

        Args:
            track_name (String): Name of the track

        Returns:
            (bool, bool): (exists, is_mp3)
        """
        track_name = self.remove_ext(track_name).lower()
        track_name = self.clean_name(track_name)

        # print(track_name)
        if track_name in self.tracks:
            return True, False
        if track_name in self.tracks_mp3:
            return True, True
        return False, False
