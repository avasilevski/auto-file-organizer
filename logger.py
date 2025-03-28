import os
from datetime import datetime
from config import LOG_DIR, LOG_FILE

def init_log():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_move(src, dest):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = os.path.basename(src)
    category = os.path.basename(os.path.dirname(dest))
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{timestamp}] Moved: {filename} → {category}/\n")