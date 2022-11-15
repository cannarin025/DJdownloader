# DJ Downloader

A program to download audio from YouTube or SoundCloud in .mp3 format

# Setup

1. Install FFMPEG
2. Clone this repository
3. *(optional)* create a virtual env using `python -m venv ./example_venv` to install dependancies to, and activate venv.
4. Install dependacnies using `pip install -r requirements.txt`
5. run `pyinstaller ./djdownloader.py` from the root of the repository. This will create an executable file located at ./dist/djdownloader.exe
6. *(optional)* Add `.\\DJdownloader\\dist\\djdownloader` to system path to call directly in command line using `djdownloader.exe`.
    **Note: `.\\` should be replaced by the path to the repository**

# Usage
**If program was added to path (step 6.):**
```
djdownloader.exe [-h] [--dir DIR] [--artists ARTISTS] query

Downloads audio from YouTube or SoundCloud in best available quality.

positional arguments:
query              Enter either: 
                   1. A valid URL to YouTube/SoundCloud content OR 
                   2. A query to search for YouTube
                      content.

optional arguments:
-h, --help         show this help message and exit
--dir DIR          Directory to download files to. Will default to current directory.
--artists ARTISTS  Names of contributing artitsts. Separate with commas.
```

**If program is not on path:**
Instead run `PATH_TO_DJDOWNLOADER.EXE [-h] [--dir DIR] [--artists ARTISTS] query` 
where PATH_TO_DJDOWNLOADER.EXE should be replaced by the path to the executable, e.g. `D:\\Code\\Projects\\DJdownloader\\dist\\djdownloader.exe`
