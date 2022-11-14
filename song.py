from PIL import Image
from typing import Dict
import os
import requests
import subprocess
import eyed3
from eyed3.id3.frames import ImageFrame
from pytube import Stream


def add_cover_art(filepath, art):
    audiofile = eyed3.load(filepath)
    art.save('cover.png')
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.png','rb').read(), 'image/png')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    os.remove('cover.png')

class Song:
    def __init__(self, title: str, best_stream: Stream or Dict, cover_art: Image):
        self.title = title
        self.best_stream = best_stream
        self.cover_art = cover_art

    def download(self, download_path: str = ''):
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
            self.best_stream.download(output_path=f'{download_path}')
            download_filepath = f'{download_path}\\{[x for x in os.listdir(download_path) if self.title in x][0]}'
            filepath = f'{download_path}\\{self.title}.mp3'
            subprocess.run(['ffmpeg', '-i', download_filepath, filepath], stdout=subprocess.DEVNULL) # convert download to mp3 and suppress output
            os.remove(download_filepath)
        add_cover_art(filepath, self.cover_art)