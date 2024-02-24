from get_song import *
import os

query = 'https://www.youtube.com/watch?v=dvgZkm1xWPE'
download_dir = 'L:/DJ/Not Itunes/Other'
artists = None

if download_dir is None:
    download_dir = os.getcwd()
if artists is not None:
    artists = [x.strip() for x in artists.split(',')]

try:
    requests.get(query) # query is a valid url
except:
    # query is not a valid URL so treat as search term
    song = get_song_from_query(query)
    song.download(download_path=download_dir, artists=artists)
try: # try downloading url as playlist 
    songs=get_songs_from_playlist(query)
    assert songs
    for song in songs:
        song.download(download_path=download_dir)
except: # download url as single song
    song = get_song_from_url(query)
    song.download(download_path=download_dir, artists=artists)

