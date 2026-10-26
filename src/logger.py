import csv
import getpass
from pathlib import Path


def log_command(log_path, command, error=""):
    """Записывает команду и ошибку в CSV-лог."""
    if not log_path:
        return

    path = Path(log_path)
    is_new = not path.exists() or path.stat().st_size == 0

    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if is_new:
            writer.writerow(["username", "command", "error"])

        writer.writerow([getpass.getuser(), command, error])
