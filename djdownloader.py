from argparse import ArgumentParser
from yt_downloader import get_song_from_url, get_song_from_query
import os
import requests

parser = ArgumentParser(description="Downloads audio from YouTube or SoundCloud in best available quality")
parser.add_argument("query")
parser.add_argument("--dir", help="Directory to download files to. Will default to current directory.")

args = parser.parse_args()

query = args.query
download_dir = args.dir

if download_dir is None:
    download_dir = os.getcwd()

try:
    requests.get(query) # query is a valid url
    song = get_song_from_url(query)
except:
    song = get_song_from_query(query) # query is not a valid URL so treat as search term

song.download(download_path=download_dir)