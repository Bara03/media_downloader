import os
import requests

def get_directory() ->str:
    dir = os.path.join(os.path.expanduser('~'),  "Downloads")
    if os.path.exists(dir):
        return dir
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_unique_filename(filepath: str, filename: str) -> str:
    fullpath = os.path.join(filepath, filename)
    if os.path.exists(fullpath):
        base_dir, ext = os.path.splitext(fullpath)
        counter = 1
        while os.path.exists(fullpath):
            fullpath = f"{base_dir} ({counter}){ext}"
            counter += 1
    return os.path.basename(fullpath)


def validate_youtube_link(link: str) -> bool:
    try:
        response = requests.get(link)
        if response.status_code == 200:
            if "youtube.com" in response.url or "youtu.be" in response.url:
                return True
        return False
    except:
        return False