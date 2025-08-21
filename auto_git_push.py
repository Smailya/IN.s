import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = r'C:\Users\ismae\OneDrive\Documents\infitineSqora\Lounge-1.0.0'
 # Change this to your local repo path

class GitAutoPusher(FileSystemEventHandler):
    def on_any_event(self, event):
        try:
            # Stage all changes
            subprocess.run(['git', 'add', '.'], cwd=REPO_PATH)
            # Commit changes
            subprocess.run(['git', 'commit', '-m', 'Auto-update: changes detected'], cwd=REPO_PATH)
            # Push to remote
            subprocess.run(['git', 'push'], cwd=REPO_PATH)
            print("Changes committed and pushed.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    event_handler = GitAutoPusher()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()
    print("Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
