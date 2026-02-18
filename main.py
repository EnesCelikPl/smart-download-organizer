from organizer.watcher import start
from organizer.config import DOWNLOADS_DIR, ORGANIZED_DIR, LOG_DIR

def main():
    print(f"Watching: {DOWNLOADS_DIR}")
    print(f"Organizing into: {ORGANIZED_DIR}")
    start(DOWNLOADS_DIR, LOG_DIR / "organizer.log")

if __name__ == "__main__":
    main()
