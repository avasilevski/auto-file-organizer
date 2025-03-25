import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WORK_PATH, FILE_TYPES

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'


def organize_downloads():
    for item in os.listdir(WORK_PATH):
        item_path = os.path.join(WORK_PATH, item)
        # Skip processed
        if os.path.isdir(item_path):
            continue
        # Skip hidden/system files
        if item.startswith('.'):
            continue
        if os.path.isfile(item_path):
            category = get_category(item)
            category_path = os.path.join(WORK_PATH, category)
            os.makedirs(category_path, exist_ok=True)
            try:
                shutil.move(item_path, os.path.join(category_path, item))
                print(f"Moved: {item} → {category}/")
            except Exception as e:
                print(f"Failed to move {item}: {e}")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            organize_downloads()
            print(f"New file: {event.src_path}")


print(f"Watching {WORK_PATH} for new files...\nPress Ctrl+C to stop.")
# Run initialy
organize_downloads()
observer = Observer()
observer.schedule(MyHandler(), path=WORK_PATH, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()