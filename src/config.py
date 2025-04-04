import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

WORK_PATH = os.getenv("WORK_PATH", str(Path.home() / "Downloads"))
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