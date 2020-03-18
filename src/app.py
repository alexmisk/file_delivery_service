import time
import os
import sys

from watcher import Watcher
from sender import Sender

if sys.platform != 'linux':
    print('This app must be executed under Linux')
    sys.exit()
    sys.exit(1)

WATCH_DIR = os.environ.get('WATCH_DIR') or str(os.getcwd()) 
FILE_HANDLER_API_ENDPOINT = os.environ.get('FILE_HANDLER_API_ENDPOINT') or 'https://localhost:3456/files'
FETCH_INTERVAL = os.environ.get('WATCH_DIR') or 1 

watcher = Watcher(dir_path=WATCH_DIR)
sender = Sender(api_endpoint=FILE_HANDLER_API_ENDPOINT)

while True:
    uploaded_files = watcher.get_uploaded_files()
    sender.send(uploaded_files, delete_after_upload=True)
    time.sleep(FETCH_INTERVAL)
