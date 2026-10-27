import hashlib
from pathlib import Path


def load_vfs(directory):
    """Загружает виртуальную файловую систему в память."""
    root = Path(directory)

    if not root.exists():
        raise FileNotFoundError(f"VFS не найдена: {directory}")

    if not root.is_dir():
        raise NotADirectoryError(f"VFS не является папкой: {directory}")

    vfs = {}

    for item in root.rglob("*"):
        if item.is_symlink():
            raise ValueError(f"Ссылки не поддерживаются: {item}")

        path = item.relative_to(root).as_posix()

        if item.is_dir():
            vfs[path] = {"type": "directory"}

        elif item.is_file():
            vfs[path] = {
                "type": "file",
                "content": item.read_bytes()
            }

    return vfs



def calculate_vfs_hash(vfs):
    """Вычисляет SHA-256 структуры и содержимого VFS."""
    digest = hashlib.sha256()

    for path in sorted(vfs):
        entry = vfs[path]

        digest.update(entry["type"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")

        if entry["type"] == "file":
            content = entry["content"]
            digest.update(len(content).to_bytes(8, "big"))
            digest.update(content)

    return digest.hexdigest()
