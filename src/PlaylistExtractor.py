import shutil
import csv
from pathlib import Path


class PlaylistExtractor:
    def __init__(self, headers, playlist, encoding="utf-8"):
        self.headers = headers
        self.playlist = playlist
        self.encoding = encoding
        play_path = Path("out", playlist + ".csv")
        tracks = []
        with open(play_path, encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if not row:
                    break
                if line_count == 0:
                    line_count += 1
                else:
                    track_info = {}
                    for i in range(len(row)):
                        track_info[headers[i]] = row[i]

                    tracks.append(track_info)

    def move_playlist_data(self):
        pass
