import os
import shutil

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

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

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'


def organize_downloads():
    for item in os.listdir(DOWNLOADS_PATH):
        item_path = os.path.join(DOWNLOADS_PATH, item)
        if os.path.isfile(item_path):
            category = get_category(item)
            category_path = os.path.join(DOWNLOADS_PATH, category)
            os.makedirs(category_path, exist_ok=True)
            try:
                shutil.move(item_path, os.path.join(category_path, item))
                print(f"Moved: {item} → {category}/")
            except Exception as e:
                print(f"Failed to move {item}: {e}")

if __name__ == "__main__":
    organize_downloads()