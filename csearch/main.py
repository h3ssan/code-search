from sys import argv
from os import path

from .db import store_cached_files
from .config import Config
from .caching import cache_repo

def set_repo_dir():
    Config.REPO_DIR = argv[1] if len(argv) > 1 else Config.REPO_DIR
    print(f"Using repository directory: {Config.REPO_DIR}")

def validate_repo_dir():
    if not path.exists(Config.REPO_DIR):
        print(f"Repository directory does not exist: {Config.REPO_DIR}")
        exit(1)

def cache_repository():
    print("Caching repository data...")
    cached_data = {}
    cache_repo(cached_data, Config.REPO_DIR)
    print(f"Cached {len(cached_data):,} files.")
    return cached_data

def store_cache(cached_data):
    print("Inserting into database...")
    store_cached_files(cached_data)
    print("Repository data cached successfully.")

def main():
    set_repo_dir()
    validate_repo_dir()
    cached_data = cache_repository()
    store_cache(cached_data)

if __name__ == "__main__":
    main()
