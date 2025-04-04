import time
from src.config import WORK_PATH
from src.watcher import WatcherHandler, Handler

print(f"Watching {WORK_PATH} for new files...\nPress Ctrl+C to stop.")

watcherHandler = WatcherHandler()
watcherHandler.on_created(Handler(), path=WORK_PATH, recursive=False)
watcherHandler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcherHandler.stop()
watcherHandler.join()