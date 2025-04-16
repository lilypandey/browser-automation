import os
import platform
from glob import glob

def get_browser_cache_paths(app):
    system = platform.system()
    paths = []
    home = os.path.expanduser("~")

    if app == "chrome":
        if system == "Linux":
            base = os.path.join(home, ".config", "google-chrome", "Profile 3")
            paths = [os.path.join(base, "Cache"), os.path.join(base, "History")]
        elif system == "Windows":
            base = os.path.join(os.getenv('LOCALAPPDATA'), "Google", "Chrome", "User Data", "Profile 3")
            paths = [os.path.join(base, "Cache"), os.path.join(base, "History")]

    elif app == "firefox":
        if system == "Linux":
            base = os.path.join(home, ".mozilla", "firefox")
            profile_dirs = glob(os.path.join(base, "*.default-release"))
            for dir in profile_dirs:
                paths.append(os.path.join(dir, "cache2"))
                paths.append(os.path.join(dir, "places.sqlite"))  
        elif system == "Windows":
            base = os.path.join(os.getenv('APPDATA'), "Mozilla", "Firefox", "Profiles")
            profile_dirs = glob(os.path.join(base, "*.default-release"))
            for dir in profile_dirs:
                paths.append(os.path.join(dir, "cache2"))
                paths.append(os.path.join(dir, "places.sqlite"))

    return paths
