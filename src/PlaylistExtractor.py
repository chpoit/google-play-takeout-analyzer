import shutil
import csv
from pathlib import Path


class PlaylistExtractor:
    def __init__(self, headers, playlist, track_loader, encoding="utf-8"):
        self.headers = headers
        self.playlist = playlist
        self.encoding = encoding
        self.track_loader = track_loader
        self.tracks_info = {"missing": [], "existing": [], "mp3": []}

        self._read_playlist_data()
        self.build_existing()

    def _read_playlist_data(self):
        play_path = Path("out", self.playlist, f"all.csv")
        self.tracks = []
        with open(play_path, encoding=self.encoding) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if not row:
                    break
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    track_info = {}
                    for i in range(len(row)):
                        track_info[self.headers[i]] = row[i]

                    self.tracks.append(track_info)

    def build_existing(self):
        for track in self.tracks:
            exists, is_mp3 = self.track_loader.contains(track["Title"])
            if not exists:
                print(track["Title"], exists, is_mp3)

            if not exists and not is_mp3:
                self.tracks_info["missing"].append(track)
            elif exists and not is_mp3:
                self.tracks_info["existing"].append(track)
            elif exists and is_mp3:
                self.tracks_info["mp3"].append(track)

    def get_missing(self):
        return self.tracks_info["missing"]

    def get_existing(self):
        return self.tracks_info["existing"]

    def get_mp3(self):
        return self.tracks_info["mp3"]
