import os
import platform
import subprocess
import shutil
from utils import get_browser_cache_paths

def open_browser(app, url):
    
    try:
        if platform.system() == "Windows":
            if app == "chrome":
                os.system(f'start chrome "{url}"')
            elif app == "firefox":
                os.system(f'start firefox "{url}"')
        elif platform.system() == "Linux":
            if app == "chrome":
                subprocess.run(["google-chrome", url])
            elif app == "firefox":
                subprocess.run(["firefox", url])
        else:
            return f"{platform.system()} not supported"
        return f"{app} opened with URL: {url}"
    except Exception as e:
        return str(e)

def close_browser(app):
    try:
        if platform.system() == "Windows":
            if app == "chrome":
                os.system("taskkill /IM chrome.exe /F")
            elif app == "firefox":
                os.system("taskkill /IM firefox.exe /F")
        elif platform.system() == "Linux":
            subprocess.run(["pkill", app])
        else:
            return f"{platform.system()} not supported"
        return f"{app} closed successfully"
    except Exception as e:
        return str(e)

def clear_browser_data(app):
    
    try:
        cache_paths = get_browser_cache_paths(app)
        for path in cache_paths:
            if os.path.isdir(path): 
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    try:
                        if os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                        elif os.path.isfile(item_path) or os.path.islink(item_path):
                            os.remove(item_path)
                    except Exception as e:
                        print(f"Failed to delete {item_path}: {e}")
            elif os.path.isfile(path):
                try:
                    os.remove(path)
                except Exception as e:
                    print(f"Failed to delete {path}: {e}")
        return f"{app} cache and history cleared"
    except Exception as e:
        return str(e)

