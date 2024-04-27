import sys
import importlib
import subprocess
from etc.config import get_packages

def check_install_packages():
    for package_name in get_packages():
        try:
            importlib.import_module(package_name)
        except ImportError:
            print(f"{package_name} is not installed. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

