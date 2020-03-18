import os
from inotify_simple import INotify, flags

class Watcher():
    def __init__(self, dir_path=str(os.getcwd())):
        self.inotify = INotify()
        self.dir_path = dir_path
        self.watch_flags = flags.CLOSE_WRITE
        self.inotify.add_watch(self.dir_path, self.watch_flags)
 
    def get_uploaded_files(self):
        uploaded_files = []
        for event in self.inotify.read():
            filename = str(event.name)
            filepath = os.path.join(str(os.getcwd()), self.dir_path, filename)
            uploaded_files.append(filepath)
        return uploaded_files
