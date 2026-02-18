import shutil
from pathlib import Path
from .logger import log_action

def move_file(file_path: Path, target_dir: Path, log_file: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / file_path.name

    if destination.exists():
        stem = file_path.stem
        suffix = file_path.suffix
        i = 1
        while True:
            destination = target_dir / f"{stem} ({i}){suffix}"
            if not destination.exists():
                break
            i += 1

    shutil.move(str(file_path), str(destination))
    log_action(log_file, f"{file_path.name} -> {destination}")
