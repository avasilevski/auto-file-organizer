import os

from src.config import FILE_TYPES

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, exts in FILE_TYPES.items():
        if ext in exts:
            return category
    return "Others"