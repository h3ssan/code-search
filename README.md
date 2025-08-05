# Simple Code Search

A simple code search tool that allows you to cache and search through code files efficiently.

## Features

- Caching of code files for faster search
- Support for various file types
- Configurable settings for ignoring files and directories

## How to Use

- Create `repositories/` directory and add your code files.
- Run `make` to run the cache command.

> Note: The `Makefile` uses a variable for the Python command to ensure compatibility across different environments. You can set the `PYTHON` variable in your environment or modify the `Makefile` to use a specific Python version.

> A `cache.db` SQLite database will be created in the root, which stores the cached code files. You can query this database to search for specific code snippets or keywords.
