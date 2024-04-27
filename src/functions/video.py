from etc.helpers import get_unique_filename, get_directory
from pytube import YouTube

def download_mp4(link: str):
    output_path = get_directory()
    print("MP4 Download started.")
    try:
        yt = YouTube(link)
        video_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution_video_stream = video_streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        filename = get_unique_filename(output_path, yt.title + ".mp4")
        highest_resolution_video_stream.download(output_path=output_path, filename=filename)
    except Exception as err:
        print(f"An error occurred while downloading.\n[Details]: {err}")
        return False
    print(f"Video successfully downloaded. Path: {output_path}")
    return True