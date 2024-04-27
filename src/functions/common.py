from typing import Callable
from etc.helpers import validate_youtube_link

def handle_download(type: str,handler_function: Callable[[str], bool]):
    while True:
        link = input(f"[{type.capitalize()} - Download] - Insert the link of the {type} you want to download (or type 'exit' to exit): ")
        if link == 'exit':
            break
        if validate_youtube_link(link):
            handler_function(link)
        else:
            print("Invalid YouTube link. Please try again.")

