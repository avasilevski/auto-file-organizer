import os
import shutil
import subprocess
from src.config import WORK_PATH, FILE_TYPES, CWD
from src.logger import log_move

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

def organize():
    for item in os.listdir(WORK_PATH):
        item_path = os.path.join(WORK_PATH, item)
        if os.path.isdir(item_path) or item.startswith("."):
            continue
        category = get_category(item)
        dest_dir = os.path.join(WORK_PATH, category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(item_path, os.path.join(dest_dir, item))
        log(item_path, os.path.join(dest_dir, item))