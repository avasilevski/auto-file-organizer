import os

# Placeholder paths (to be overridden in config.local.py)
WORK_PATH = os.getenv("WORK_PATH", "~/Downloads")
LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE = os.path.join(LOG_DIR, os.getenv("LOG_FILE", "file_organizer.log"))
CWD = os.getenv("CWD", "/path/to/cpp")

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.dmg', '.pkg'],
    'Scripts': ['.py', '.sh', '.bat'],
    'Others': []
}

try:
    from config.local import *  # Override any variables if config.local.py exists
except ImportError:
    pass