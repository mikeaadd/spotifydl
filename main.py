
import spotdl.console
import spotdl.console.sync
import typer
import spotdl
from pathlib import Path
import os
import subprocess


def main(spotify_link, folder):
    if not spotify_link.startswith("https://open.spotify.com/playlist/"):
        raise Exception("Invalid Spotify playlist: The link should start with `https://open.spotify.com/playlist/`")
    playlist_id = (
        spotify_link
        .removeprefix("https://open.spotify.com/playlist/")
        .split("?")
        [0]
    )

    # create directory if not exists, change to right directory
    path = Path(f"{os.getcwd()}/{folder}")
    Path(path).mkdir(parents=True, exist_ok=True)
    os.chdir(path)
    
    subprocess.run(['spotdl', spotify_link, "--save-file", "music.spotdl"])

if __name__ == "__main__":
    typer.run(main)