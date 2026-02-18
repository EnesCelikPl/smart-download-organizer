import subprocess
from pathlib import Path

PLIST = Path.home() / "Library" / "LaunchAgents" / "com.enes.smartorganizer.plist"

def run(cmd):
    subprocess.run(cmd, check=False)

def start():
    run(["launchctl", "load", str(PLIST)])

def stop():
    run(["launchctl", "unload", str(PLIST)])

def status():
    p = subprocess.run(["launchctl", "list"], capture_output=True, text=True)
    lines = [l for l in p.stdout.splitlines() if "com.enes.smartorganizer" in l]
    if lines:
        print(lines[0])
    else:
        print("not running")

def main():
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "start":
        start()
    elif cmd == "stop":
        stop()
    elif cmd == "status":
        status()
    else:
        print("usage: python cli.py start|stop|status")

if __name__ == "__main__":
    main()
