import os
import shutil
import subprocess
from src.config import WORK_PATH, FILE_TYPES, CWD

def log(src, dest):
    filename = os.path.basename(src)
    category = os.path.basename(os.path.dirname(dest))
    # Call to the C++ subprocess
    cmd_arg = f"Moved: {filename} → {category}/"
    subprocess.run(
        ["../build/main.out", cmd_arg],
        cwd=CWD
    )

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, exts in FILE_TYPES.items():
        if ext in exts:
            return category
    return "Others"

def organize(file_path):
    if os.path.isdir(file_path) or os.path.basename(file_path).startswith("."):
        return
    category = get_category(file_path)
    dest_dir = os.path.join(WORK_PATH, category)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(file_path))
    shutil.move(file_path, dest_path)
    log(file_path, dest_path)