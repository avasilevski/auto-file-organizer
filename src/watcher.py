from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from src.organizer import organize
from src.analyzer import analyze

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)
            analyze(event.src_path)
            organize(event.src_path)

class WatcherHandler:
    def __init__(self):
        self.observer = Observer()

    def on_created(self, handler, path, recursive=False):
        self.observer.schedule(handler, path, recursive=recursive)

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()

    def join(self):
        self.observer.join()