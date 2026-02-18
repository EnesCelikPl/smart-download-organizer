from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DOWNLOADS_DIR = Path.home() / "Downloads"
ORGANIZED_DIR = DOWNLOADS_DIR / "Organized"

RULES_FILE = BASE_DIR / "config" / "rules.yaml"
LOG_DIR = BASE_DIR / "logs"
HASH_DB = LOG_DIR / "hashes.txt"
