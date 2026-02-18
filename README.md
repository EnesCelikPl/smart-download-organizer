# Smart Download Organizer (macOS)

Watches the macOS Downloads folder and automatically moves files into categorized folders.
Uses YAML rules for categories and SHA-256 hashing to detect duplicates.

## Features
- Real-time monitoring (watchdog)
- Configurable categories via `config/rules.yaml`
- Duplicate detection (SHA-256) -> moves to `Duplicates/`
- Runs on boot using macOS LaunchAgent

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
