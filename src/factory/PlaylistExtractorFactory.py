import os
from pathlib import Path
from PlaylistExtractor import PlaylistExtractor


class PlaylistExtractorFactory:
    def create_extractor(self, config, playlist, encoding="utf-8"):
        headers = config["csv-headers"]

        return PlaylistExtractor(headers, playlist, encoding)
