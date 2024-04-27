import sys
from etc.libraries import check_install_packages
check_install_packages()
from functions.common import handle_download
from functions.audio import download_mp3
from functions.video import download_mp4


if len(sys.argv) != 2:
    print("Usage: python3 media_download.py [audio|video]")
    sys.exit(1)

run_parameter = sys.argv[1]
print("[Bara media downloader]\n")
match run_parameter:
    case "audio":
        handle_download(run_parameter, download_mp3)
    case "video":
        handle_download(run_parameter, download_mp4)
    case _:
        print("Invalid parameter. Please specify 'audio' or 'video'.")


