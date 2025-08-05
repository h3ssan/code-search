from typing import Dict


FILE_TYPES: Dict[str, str] = {
    'txt': 'text',
    'json': 'json',
    'py': 'python',
    'md': 'markdown',
    'html': 'html',
    'css': 'css',
    'js': 'javascript',
    'xml': 'xml',
    'csv': 'csv',
    'c': 'c',''
    'proto': 'protobuf',
    'h': 'c_header',
    'cpp': 'cpp',
    'java': 'java',
    'go': 'go',
    'sh': 'shell',
    'rb': 'ruby',
    'php': 'php',
    'rs': 'rust',
    'swift': 'swift',
    'ts': 'typescript',
    'yaml': 'yaml',
    'yml': 'yaml',
    'jpg': 'image',
    'jpeg': 'image',
    'png': 'image',
    'gif': 'image',
    'bmp': 'image',
    'svg': 'image',
    'pdf': 'document',
    'docx': 'document',
    'xlsx': 'document',
    'pptx': 'document',
    'zip': 'archive',
    'tar': 'archive',
    'gz': 'archive',
    'rar': 'archive',
    '7z': 'archive',
    'thrift': 'Apache Thrift',
    'excalidraw': 'Excalidraw',
    'cmake': 'CMake',
    'vim': 'Vim script',
}

FILE_NAME_TYPES: Dict[str, str] = {
    'README.md': 'Readme',
    'LICENSE': 'License',
    'Makefile': 'Makefile',
    'Dockerfile': 'Dockerfile',
    'package.json': 'NPM package manifest',
    'requirements.txt': 'Python requirements',
    'Gemfile': 'Ruby Gemfile',
    'pom.xml': 'Maven POM',
    'build.gradle': 'Gradle build',
    'setup.py': 'Python setup script',
    'config.json': 'Configuration',
    'settings.json': 'Settings',
    'tsconfig.json': 'TypeScript config',
    'webpack.config.js': 'Webpack config',
    'babel.config.js': 'Babel config',
    'eslint.config.js': 'ESLint config',
    'prettier.config.js': 'Prettier config',
    'gitignore': 'Git ignore',
    'docker-compose.yml': 'Docker Compose',
}

def get_file_ext(file_path: str) -> str:
    return file_path.split('.')[-1].lower() if '.' in file_path else 'unknown'

def get_file_type(file_path: str) -> str:
    file_name = file_path.split('/')[-1]
    if file_name in FILE_NAME_TYPES:
        return FILE_NAME_TYPES[file_name]

    file_extension = get_file_ext(file_path)
    return FILE_TYPES.get(file_extension, 'unknown')

def is_binary(file_path: str) -> bool:
    """
    Check if a file is binary based on its content
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:  # Null byte indicates binary
                return True
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return False