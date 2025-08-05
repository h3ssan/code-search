from sqlite3 import connect, OperationalError
from typing import Dict

from .types import CachedFile
from .config import DBConfig

def create_db():
    """
    Creates a SQLite database and a table for cached files.
    """
    conn = connect(DBConfig.DB_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DBConfig.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE,
                file_type TEXT,
                file_ext TEXT,
                size_bytes INTEGER,
                content BLOB
            )
        """)
        conn.commit()
    except OperationalError as e:
        print(f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


def insert_cached_file(cursor, file_path: str, cached_file: dict):
    """
    Inserts a cached file into the database.
    """

    try:
        cursor.execute(f"""
            INSERT OR IGNORE INTO {DBConfig.TABLE_NAME} (file_path, file_type, file_ext, size_bytes, content)
            VALUES (?, ?, ?, ?, ?)
        """, (file_path, cached_file.get("type"), cached_file.get("ext"), cached_file.get("size_bytes"), cached_file.get("content")))
    except OperationalError as e:
        print(f"Database error: {e}")


def store_cached_files(cached_files: Dict[str, CachedFile]):
    """
    Stores a list of cached files into the database.
    """
    create_db()

    conn = connect(DBConfig.DB_FILE)
    cursor = conn.cursor()

    for file_path, cached_file in cached_files.items():
        insert_cached_file(cursor, file_path, cached_file.to_dict())

    conn.commit()
    cursor.close()
    conn.close()