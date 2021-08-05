import os
import csv
from pathlib import Path


class PlaylistWriter:
    def __init__(self, config):
        self.headers = config["csv-headers"]

        os.makedirs("out", exist_ok=True)

    def write_playlists(self, playlists):
        paths = []
        for playlist in playlists:
            print(playlist)
            paths += self.write_playlist(playlist, playlists[playlist])

        return paths

    def write_playlist(self, playlist_name, playlist_tracks):
        sorted_tracks = sorted(playlist_tracks, key=lambda x: int(x["Playlist Index"]))

        out_file = Path("out", playlist_name + ".csv")
        with open(out_file, "w", encoding="utf-8", newline="\n") as f:
            csv_writer = csv.writer(f, delimiter=",")
            csv_writer.writerow(self.headers)
            playlist_rows = map(
                lambda row: [row[i] for i in self.headers], sorted_tracks
            )
            for row in playlist_rows:
                print(row)
                csv_writer.writerow(row)

        return out_file
