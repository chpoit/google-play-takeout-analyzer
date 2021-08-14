# google-play-takeout-analyzer

Simple scripts that read the data from playlits taken from a Google Play Music data takeout and outputs lists of songs that you might want to buy to actually own them now that only youtube music exists.

Run the `src/main.py` file to create your lists.

Set the path to your takeout in the `config.json` file.

Three files per playlist are created:
- `out/<PLAYLIST>/missing.csv`: No file was found for the tracks in this file.
- `out/<PLAYLIST>/existing.csv`: A csv file with data was found for the tracks in this file.
- `out/<PLAYLIST>/mp3.csv`: A mp3 file was found for the tracks in this file.