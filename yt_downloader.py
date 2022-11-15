
from typing import Dict, List
from song import Song
from youtube_dl import YoutubeDL
from pytube import YouTube, Search
from PIL import Image
import requests
import datetime


def get_best_stream_YoutubeDL(streams: Dict) -> Dict:
    best = streams[0]
    for stream in streams:
        if stream['abr'] > best['abr']:
            best = stream
    return stream

def get_song_YoutubeDL(url: str) -> Song:
    with YoutubeDL({'format':'bestaudio/best', 'noplaylist': 'True'}) as ydl:
            video_data = ydl.extract_info(url, download=False) # url was supplied so video can be directly extracted
            audio_streams = [x for x in video_data['formats'] if 'abr' in x.keys() and x['vcodec'] == 'none'] # select only audio streams
            title = video_data['title']
            cover_art = Image.open(requests.get(video_data['thumbnails'][-1]['url'], stream=True).raw)
            best_stream = get_best_stream_YoutubeDL(audio_streams)
    return Song(title, best_stream, cover_art)

def get_song_pytube(video: YouTube) -> Song:
    best_stream = video.streams.filter(type='audio').order_by('abr').last()  # Get highest quality stream
    title = video.title
    cover_art = Image.open(requests.get(video.thumbnail_url, stream=True).raw)
    return Song(title, best_stream, cover_art)

def get_song_from_url(url: str) -> Song:
    if 'SOUNDCLOUD' in url.upper():
        return get_song_YoutubeDL(url)
    video = YouTube(f"{url}")
    return get_song_pytube(video)

def get_song_from_query(query: str) -> Song:
    s = Search(query)
    non_livestream_results = [video for video in s.results if 'reason' not in list(video.vid_info['playabilityStatus'].keys())] # ignore livestreams 
    for i, video in enumerate(non_livestream_results):
        best_abr = video.streams.filter(type='audio').order_by('abr').last().abr
        print(f"{i+1}. Title: {video.title}\n{(len(str(i+1))+2) * ' '}Best abr: {best_abr}\n{(len(str(i+1))+2) * ' '}Duration: {str(datetime.timedelta(seconds=video.length))}\n")
    selected_index = int(input("Please enter a video index to continue: ")) - 1
    video = s.results[selected_index]
    return get_song_pytube(video)