import os
import csv
from pathlib import Path


class PlaylistWriter:
    def __init__(self, config):
        self.headers = config.headers

        os.makedirs("out", exist_ok=True)

    def write_playlists(self, playlists):
        paths = []
        for playlist in playlists:
            new_file = self.write_playlist(playlist, playlists[playlist])
            paths.append(new_file)

        return paths

    def write_playlist(self, playlist_name, playlist_tracks):
        out_file = self._write_file(playlist_name, playlist_tracks)

        return out_file

    def _write_file(self, playlist_name, playlist_tracks, filename="all"):
        sorted_tracks = sorted(playlist_tracks, key=lambda x: x["Title"])
        if not filename:
            filename = playlist_name

        out_dir = Path("out", playlist_name)
        out_file = Path(out_dir, f"{filename}.csv")
        os.makedirs(out_dir, exist_ok=True)
        with open(out_file, "w", encoding="utf-8", newline="\n") as f:
            csv_writer = csv.writer(f, delimiter=",")
            csv_writer.writerow(self.headers)
            playlist_rows = map(
                lambda row: [row[i] for i in self.headers], sorted_tracks
            )
            for row in playlist_rows:
                csv_writer.writerow(row)

        return out_file

    def write_missing_existing(self, playlist_extractor):
        playlist_name = playlist_extractor.playlist

        missing = playlist_extractor.get_missing()
        existing = playlist_extractor.get_existing()
        mp3 = playlist_extractor.get_mp3()

        self._write_file(playlist_name, missing, "missing")
        self._write_file(playlist_name, existing, "existing")
        self._write_file(playlist_name, mp3, "mp3")
