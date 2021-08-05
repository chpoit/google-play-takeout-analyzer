import shutil
import csv
from pathlib import Path


class PlaylistExtractor:
    def __init__(self, headers, playlist, encoding="utf-8"):
        self.headers = headers
        self.playlist = playlist
        self.encoding = encoding

        self._read_playlist_data()

    def _read_playlist_data(self):
        play_path = Path("out", self.playlist + ".csv")
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

    def move_playlist_data(self):
        pass
