from os import path, listdir

from .file_type import get_file_type, get_file_ext, is_binary
from .config import Config
from .types import CachedFile

def cache_file(cached_data: dict, file_path: str):
    file_type = get_file_type(file_path)
    file_extension = get_file_ext(file_path)
    size_bytes = path.getsize(file_path)
    file_path_relative = file_path.lstrip(Config.REPO_DIR + path.sep)

    if Config.IGNORE_BINARY and is_binary(file_path):
        return
    
    if Config.IGNORE_UNKNOWN_EXT and (file_extension == "unknown" or file_type == "unknown"):
        return
    
    if Config.IGNORE_IMAGES and file_type == "image":
        return
    
    if Config.IGNORE_EMPTY_FILES and size_bytes == 0:
        return
    
    with open(file_path, 'r', encoding=Config.ENCODING, errors="replace") as file:
        content = file.read()

    cached_data[file_path_relative] = CachedFile(
        file_type=file_type,
        file_ext=file_extension,
        size_bytes=size_bytes,
        content=content
    )


def cache_repo(cached_data: dict, dir_path: str):
    """
    Caches repository data into a dictionary.
    """
    for item in listdir(dir_path):
        if item.startswith('.') and Config.IGNORE_HIDDEN:
            continue

        item_path = path.join(dir_path, item)
        if path.isdir(item_path) and item not in Config.IGNORE_DIRS:
            cache_repo(cached_data, item_path)
        else:
            if item in Config.IGNORE_FILES:
                print(f"Skipping ignored file: {item}")
                continue
            
            cache_file(cached_data, item_path)
