# DJ Downloader

A program to download audio from YouTube or SoundCloud in .mp3 format

# Setup

1. [Install FFMPEG](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
2. Clone this repository.
3. *(optional)* create a virtual env using `python -m venv ./example_venv` to install dependancies to, and activate the virtual env.
4. Install dependacnies using `pip install -r requirements.txt`.
5. run `pyinstaller ./djdownloader.py` from the root of the repository. This will create an executable file located at `.\dist\djdownloader.exe`.
6. *(optional)* Add `[PATH TO REPOSITORY]\DJdownloader\dist\djdownloader` to system path to call directly in command line using `djdownloader.exe`.

    This can be done by opening cmd as administrator and running the following: 
    
    `setx /m PATH "[PATH TO REPOSITORY]\dist\djdownloader;%PATH%"`.

    **Note: `[PATH TO REPOSITORY]` should be replaced with the suitable path, e.g. `D:\Code\Projects\DJdownloader`.**
7. Restart system

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
where PATH_TO_DJDOWNLOADER.EXE should be replaced by the path to the executable, e.g. `D:\Code\Projects\DJdownloader\dist\djdownloader.exe`.

## Example usage:
### Query Example:

```
L:\DJ\Not Itunes\Other> djdownloader.exe 'these nights loud luxury extended' --artists 'Loud Luxury, KIDDO'
1. Title: These Nights (Extended Mix)
   Best abr: 160kbps
   Duration: 0:03:25
   Views: 11204
   Channel: Loud Luxury - Topic

2. Title: Loud Luxury Feat. KIDDO - These Nights (Extended Mix)
   Best abr: 160kbps
   Duration: 0:03:27
   Views: 2223
   Channel: GeloDJ - Music Promotion

3. Title: Loud Luxury feat. KIDDO - These Nights (Official Music Video)
   Best abr: 160kbps
   Duration: 0:02:24
   Views: 378025
   Channel: Armada Music TV

Please enter a video index to continue: 1
Downloading!...
Done!
File downloaded at: L:\DJ\Not Itunes\Other\These Nights (Extended Mix).mp3!
```

### URL Example:
```
L:\DJ\Not Itunes\Other> djdownloader.exe 'https://www.youtube.com/watch?v=Y7592KzLLDU' --artists 'Disciples'
Downloading!...
Done!
File downloaded at: L:\DJ\Not Itunes\Other\Disciples - On My Mind (Extended Mix).mp3!
```

# Known Bugs:
The error: `IndexError: tuple index out of range` can be thrown when `pyinstaller ./djdownloader.py` is run. This is a Python 3.10 error with the following [solution](https://www.example.com).
To fix this error, open `C:\Python310\Lib\dis.py` and create a new line after line 431 with `extended_arg = 0` such that the code reads:

```py
else:
    arg = None
    extended_arg = 0
yield(i, op, arg)
```