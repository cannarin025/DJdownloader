from PIL import Image
from typing import Dict
import os
import requests
import subprocess
import eyed3
from eyed3.id3.frames import ImageFrame
from pytube import Stream
from typing import List


def add_cover_art(filepath: str, art) -> None:
    audiofile = eyed3.load(filepath)
    art.save('cover.png')
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.png','rb').read(), 'image/png')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    os.remove('cover.png')

def add_artists(filepath: str, artists: List[str]) -> None:
    audiofile = eyed3.load(filepath)
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.artist = '/'.join(artists)
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

class Song:
    def __init__(self, title: str, best_stream: Stream or Dict, cover_art: Image):
        self.title = title
        self.best_stream = best_stream
        self.cover_art = cover_art

    def download(self, download_path: str = '', artists = None):
        if not download_path:
            download_path = os.getcwd()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77'}
        print("Downloading!...")
        if type(self.best_stream) is dict:
            audio = requests.get(self.best_stream['url'], headers, timeout=None)
            filepath = f'{download_path}\\{self.title}.mp3'
            open(filepath, 'wb').write(audio.content)
            print(f'Downloaded file as: {filepath}!')
        else:
            download_filepath = self.best_stream.download(output_path=f'{download_path}')
            mp3_filepath = f'{download_path}\\{self.title}.mp3'
            subprocess.run(['ffmpeg', '-i', download_filepath, mp3_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # convert download to mp3 and suppress output
            os.remove(download_filepath)
        add_cover_art(mp3_filepath, self.cover_art)
        if artists: add_artists(mp3_filepath, artists)
        print(f"Done!\nFile downloaded at: {mp3_filepath}!")