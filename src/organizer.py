import os
import shutil
import subprocess
from src.config import WORK_PATH, CWD

def log(src, dest):
    filename = os.path.basename(src)
    category = os.path.basename(os.path.dirname(dest))
    # Call to the C++ subprocess
    cmd_arg = f"Moved: {filename} → {category}/"
    subprocess.run(
        ["../build/main.out", cmd_arg],
        cwd=CWD
    )

def organize(file_path, category):
    if os.path.isdir(file_path) or os.path.basename(file_path).startswith("."):
        return
    dest_dir = os.path.join(WORK_PATH, category)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(file_path))
    shutil.move(file_path, dest_path)
    log(file_path, dest_path)