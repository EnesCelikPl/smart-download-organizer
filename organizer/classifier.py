from pathlib import Path
import yaml
from .config import RULES_FILE

def load_rules() -> dict:
    data = yaml.safe_load(RULES_FILE.read_text(encoding="utf-8"))
    return {k: {e.lower() for e in v} for k, v in data.items()}

RULES = load_rules()

def classify(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    for category, exts in RULES.items():
        if ext in exts:
            return category
    return "Others"
