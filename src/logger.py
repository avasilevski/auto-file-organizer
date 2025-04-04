import os
import subprocess
from datetime import datetime
from src.config import LOG_DIR, LOG_FILE, CWD

def init_log():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_move(src, dest):
    filename = os.path.basename(src)
    category = os.path.basename(os.path.dirname(dest))
    # Call to the C++ subprocess
    cmd_arg = f"Moved: {filename} → {category}/"
    subprocess.run(
        ["../build/main.out", cmd_arg],
        cwd=CWD
    )