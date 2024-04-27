from etc.helpers import get_unique_filename, get_directory
from pytube import YouTube

def download_mp3(link: str):
    output_path = get_directory()
    print("MP3 Download started.")
    try:
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}")
        filename = get_unique_filename(output_path, yt.title + ".mp3")
        audio_stream.download(output_path=output_path, filename=filename)
    except Exception as err:
        print(f"An error occurred while downloading.\n [Details]: {err}")
        return False
    print(f"Audio successfully downloaded. Path: {output_path}")
    return True