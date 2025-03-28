import os

WORK_PATH = os.path.expanduser("~/Downloads")
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "file_organizer.log")

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