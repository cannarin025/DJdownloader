from PIL import Image
import os
import requests
import eyed3
from eyed3.id3.frames import ImageFrame

class Song:
    def __init__(self, title: str, best_stream: Stream, cover_art: Image):
        self.title = title
        self.best_stream = best_stream
        self.cover_art = cover_art

    def download(self, download_path: str = ''):
        if not download_path:
            download_path = os.getcwd()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77'}
        print("Downloading!...")
        audio = requests.get(self.best_stream['url'], headers, timeout=None)
        filepath = f'{download_path}/{self.title}.mp3'
        open(filepath, 'wb').write(audio.content)
        print(f'Downloaded file as: {filepath}!')
        
        audiofile = eyed3.load(filepath)
        if (audiofile.tag == None):
            audiofile.initTag()
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.jpg','rb').read(), 'image/jpeg')
        audiofile.tag.save()