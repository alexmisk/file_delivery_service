import os

class Sender():
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint

    def send(self, files, delete_after_upload=False):
        for file in files:
            #TODO: Put actual code here
            print(f'File {file} sent over {self.api_endpoint}') 
            if delete_after_upload:
                os.remove(file)
