# Smart Download Organizer (macOS)

A background automation tool that monitors the macOS Downloads folder and automatically categorizes files into structured directories in real time.

Built with Python, watchdog, YAML configuration, and SHA-256 hashing for duplicate detection. Runs automatically on system login using macOS LaunchAgent.

---

## Features

- Real-time file monitoring (watchdog)
- Configurable categories via `config/rules.yaml`
- SHA-256 duplicate detection → moves duplicates to `Duplicates/`
- Automatic startup using macOS LaunchAgent
- Logging system for traceability
- CLI support (`start`, `stop`, `status`)
- Modular architecture
- YAML-based configuration

---

## How It Works

1. Watches the `~/Downloads` directory.
2. Matches files against category rules.
3. Moves files into structured folders:
   - Documents
   - Images
   - Videos
   - Archives
   - Audio
   - Others
4. Computes SHA-256 hash to detect duplicates.
5. Moves duplicates to `Duplicates/`.

---

## Folder Structure

Downloads/
└── Organized/
    ├── Documents/
    ├── Images/
    ├── Videos/
    ├── Archives/
    ├── Audio/
    ├── Others/
    └── Duplicates/

---

## Installation

Clone the repository:

git clone git@github.com:EnesCelikPl/smart-download-organizer.git  
cd smart-download-organizer  

Create virtual environment:

python3 -m venv venv  
source venv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

---

## Run

Start the organizer:

python src/main.py start  

Stop:

python src/main.py stop  

Check status:

python src/main.py status  

---

## Configuration

Edit file categories inside:

config/rules.yaml  

You can define:
- File extensions
- Destination folders
- Custom rules

---

## Technologies Used

- Python
- watchdog
- PyYAML
- hashlib (SHA-256)
- macOS LaunchAgent

---

## Future Improvements

- GUI version
- Cross-platform support
- Background daemon service
- Smart AI-based categorization

---

Author: Enes Celik  
