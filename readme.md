# H1 DJ Downloader

A program to download audio from YouTube or SoundCloud in .mp3 format

# Setup

1. Install FFMPEG
2. Clone this repository
3. run `pyinstaller ./djdownloader.py` from the root of the repository. This will create an executable file located at ./dist/djdownloader.exe
4. *(optional)* Add `D:\\Code\\Projects\\DJdownloader\\dist\\djdownloader` to system path to call directly in command line using `djdownloader.exe`.

# Usage
```
{
    djdownloader.exe [-h] [--dir DIR] [--artists ARTISTS] query

    Downloads audio from YouTube or SoundCloud in best available quality.

    positional arguments:
    query              Enter either: 1. A valid URL to YouTube/SoundCloud content OR 2. A query to search for YouTube
                        content.

    optional arguments:
    -h, --help         show this help message and exit
    --dir DIR          Directory to download files to. Will default to current directory.
    --artists ARTISTS  Names of contributing artitsts. Separate with commas.
}
```