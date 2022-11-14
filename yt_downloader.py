
from typing import Dict, List
from song import Song
from youtube_dl import YoutubeDL
from PIL import Image
import requests
import datetime


def get_best_stream(streams: Dict) -> Dict:
    best = streams[0]
    for stream in streams:
        if stream['abr'] > best['abr']:
            best = stream
    return stream

def get_song(query: str, num_results = 10) -> Song:
    with YoutubeDL({'format':'bestaudio/best', 'noplaylist': 'True'}) as ydl:
        try:
            requests.get(query) # checks to see if query is a valid URL
        except:
            video_data_list = ydl.extract_info(f"ytsearch{num_results}:{query}", download=False)['entries'] # searches youtube with query string to get list of videos
            for i, video_data in enumerate(video_data_list):
                audio_streams = [x for x in video_data['formats'] if 'abr' in x.keys() and x['vcodec'] == 'none']
                best_abr = audio_streams[0]['abr']
                for stream in audio_streams:
                    if stream['abr'] > best_abr:
                        best_abr = stream['abr']
                print(f"{i+1}. Title: {video_data['title']}\n{(len(str(i+1))+2) * ' '}Best abr: {best_abr}\n{(len(str(i+1))+2) * ' '}Duration: {str(datetime.timedelta(seconds=video_data['duration']))}\n")
            selected_index = int(input("Please enter a video index to continue: ")) - 1
            video_data = video_data_list[selected_index]
        else:
            video_data = ydl.extract_info(query, download=False) # url was supplied so video can be directly extracted
    
    audio_streams = [x for x in video_data['formats'] if 'abr' in x.keys() and x['vcodec'] == 'none'] # select only audio streams

    title = video_data['title']
    cover_art = Image.open(requests.get(video_data['thumbnails'][-1]['url'], stream=True).raw)
    best_stream = get_best_stream(audio_streams)

    return Song(title, best_stream, cover_art) 

song = get_song('https://www.youtube.com/watch?v=c0PZxWO33_Q')
# song = get_song('https://soundcloud.com/alpha-shitlord/jelly')
# song = get_song('bustin makes me feel good')
song.download()