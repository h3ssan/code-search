# Data structure to hold database configuration
class DBConfig:
    DB_FILE = "cache.db"
    TABLE_NAME = "cached_files"

# Data structure to hold configuration settings
class Config:
    ENCODING = "UTF-8"
    REPO_DIR = "repositories"
    IGNORE_HIDDEN = True
    IGNORE_UNKNOWN_EXT = True
    IGNORE_BINARY = True
    IGNORE_IMAGES = True
    IGNORE_EMPTY_FILES = True
    IGNORE_DIRS = ('.git', '__pycache__', '.vscode', '.idea')
    IGNORE_FILES = ('.DS_Store', 'Thumbs.db')
