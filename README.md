# Smart Download Organizer (macOS)

A background automation tool that monitors the macOS Downloads folder and automatically categorizes files into structured directories in real time.

Built with Python, watchdog, YAML configuration, and SHA-256 hashing for duplicate detection. Runs automatically on system login via macOS LaunchAgent.

---

## Features

- Real-time file monitoring (watchdog)
- Configurable categories via `config/rules.yaml`
- SHA-256 duplicate detection → moves duplicates to `Duplicates/`
- Automatic startup using macOS LaunchAgent
- Logging system for traceability
- CLI support (`start`, `stop`, `status`)

---

## 📂 Folder Structure
Downloads/
Organized/
Documents/
Images/
Videos/
Archives/
Audio/
Others/
Duplicates/
---

## Installation

```bash
git clone git@github.com:EnesCelikPl/smart-download-organizer.git
cd smart-download-organizer

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
