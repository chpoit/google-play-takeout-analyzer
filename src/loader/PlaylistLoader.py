import csv
import os
from pathlib import Path


class PlaylistLoader:
    def load_playlist_tracks(self, playlist_path):
        # If they are in a subfolder
        if Path(playlist_path, "Tracks").exists():
            playlist_path = Path(playlist_path, "Tracks")

        track_list = []

        for track_path in os.scandir(playlist_path):
            track_path = Path(playlist_path, track_path)
            track_list += self.load_playlist_track_csv(track_path)
        return track_list

    def load_playlist_track_csv(self, track_path):
        with open(track_path, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            header = []
            tracks = []
            for row in csv_reader:
                if not row:
                    break
                if line_count == 0:
                    line_count += 1
                    header = row
                else:
                    track_info = {}
                    for i in range(len(row)):
                        track_info[header[i]] = row[i]

                    tracks.append(track_info)
        return tracks
