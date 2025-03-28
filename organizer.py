import os
import shutil
from config import WORK_PATH, FILE_TYPES
from logger import log_move

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
        log_move(item_path, os.path.join(dest_dir, item))