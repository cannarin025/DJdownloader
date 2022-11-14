from PIL import Image
from typing import Dict
import os
import requests
import eyed3
from eyed3.id3.frames import ImageFrame


def add_cover_art(filepath, art):
    audiofile = eyed3.load(filepath)
    art.save('cover.png')
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.png','rb').read(), 'image/png')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    os.remove('cover.png')

class Song:
    def __init__(self, title: str, best_stream: Dict, cover_art: Image):
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
        
        self.cover_art.save('test.png')
        data = open('test.png', 'rb').read()
        # add_cover_art(filepath, artpath='D:/Code/Projects/DJdownloader/test.png')
        add_cover_art(filepath, self.cover_art)

        # audio = MP3(filepath, ID3=ID3)
        # # add ID3 tag if it doesn't exist
        # try:
        #     audio.add_tags()
        # except error:
        #     pass
        # audio.tags.add(
        #     APIC(
        #         encoding=3, # 3 is for utf-8
        #         mime='image/png', # image/jpeg or image/png
        #         type=3, # 3 is for the cover image
        #         desc=u'Cover',
        #         data=data
        #     )
        # )
        # audio.save()

        # audiofile = eyed3.load(filepath)
        # if (audiofile.tag == None):
        #     audiofile.initTag()
        # #self.cover_art.tobytes()
        # audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('test.jpg', 'rb').read(), 'image/jpeg')
        # audiofile.tag.save()