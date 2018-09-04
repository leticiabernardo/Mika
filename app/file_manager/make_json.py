import json
import pickle


class MakeJson:
    def __init__(self):
        self.folder_files = "../files/vocabulary/"

    def save_data(self, file, data):

        with open(self.folder_files + file, 'a') as f:

            str = json.dumps(data).replace('{', ',', 1)
            f.seek(-2, 2)
            f.write(str)
