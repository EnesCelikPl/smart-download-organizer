import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .classifier import classify
from .mover import move_file
from .config import ORGANIZED_DIR, HASH_DB
from .hasher import file_hash

RECENT = {}
WINDOW = 3.0

def seen_before(h: str) -> bool:
    HASH_DB.parent.mkdir(parents=True, exist_ok=True)
    if not HASH_DB.exists():
        return False
    return h in HASH_DB.read_text(encoding="utf-8").splitlines()

def remember(h: str) -> None:
    HASH_DB.parent.mkdir(parents=True, exist_ok=True)
    with HASH_DB.open("a", encoding="utf-8") as f:
        f.write(h + "\n")

def recently_processed(h: str) -> bool:
    now = time.time()
    for k, t in list(RECENT.items()):
        if now - t > WINDOW:
            del RECENT[k]
    t = RECENT.get(h)
    if t is not None and now - t < WINDOW:
        return True
    RECENT[h] = now
    return False

def handle_file(path: Path, log_file: Path) -> None:
    if path.suffix.lower() in {".crdownload", ".part", ".tmp"}:
        return
    time.sleep(1)
    if not path.exists():
        return

    h = file_hash(path)
    if recently_processed(h):
        return

    if seen_before(h):
        move_file(path, ORGANIZED_DIR / "Duplicates", log_file)
        return

    remember(h)
    category = classify(path)
    move_file(path, ORGANIZED_DIR / category, log_file)

class Handler(FileSystemEventHandler):
    def __init__(self, log_file: Path):
        self.log_file = log_file

    def on_created(self, event):
        if event.is_directory:
            return
        handle_file(Path(event.src_path), self.log_file)

    def on_moved(self, event):
        if getattr(event, "is_directory", False):
            return
        handle_file(Path(event.dest_path), self.log_file)

def start(downloads_dir: Path, log_file: Path) -> None:
    observer = Observer()
    observer.schedule(Handler(log_file), str(downloads_dir), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
