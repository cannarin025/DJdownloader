from argparse import ArgumentParser
from get_song import get_song_from_url, get_song_from_query
import os
import requests
import sys

class Parser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = Parser(description="Downloads audio from YouTube or SoundCloud in best available quality.")
parser.add_argument("query", help="Enter either: 1. A valid URL to YouTube/SoundCloud content OR 2. A query to search for YouTube content.")
parser.add_argument("--dir", help="Directory to download files to. Will default to current directory.")
parser.add_argument("--artists", help="Names of contributing artitsts. Separate with commas.")

args = parser.parse_args()

query = args.query
download_dir = args.dir
artists = args.artists

if download_dir is None:
    download_dir = os.getcwd()
if artists is not None:
    artists = [x.strip() for x in artists.split(',')]

try:
    requests.get(query) # query is a valid url
    song = get_song_from_url(query)
except:
    song = get_song_from_query(query) # query is not a valid URL so treat as search term

song.download(download_path=download_dir, artists=artists)