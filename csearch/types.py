class CachedFile:
    def __init__(self, *, file_type: str, file_ext: str, size_bytes: int, content: str):
        self.type = file_type
        self.ext = file_ext
        self.size_bytes = size_bytes
        self.content = content

    def to_dict(self):
        return {
            "type": self.type,
            "ext": self.ext,
            "size_bytes": self.size_bytes,
            "content": self.content
        }

    def __repr__(self):
        return f"CachedFile({self.to_dict()})"