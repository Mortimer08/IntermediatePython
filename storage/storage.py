import os.path


class Storage:
    def __init__(self):
        pass

    def save(self):
        print('data_saved')

    def load(self):
        print('data_loaded')


class FileStorage(Storage):
    def __init__(self):
        path = open(os.path.normpath('data/data_path.txt'), 'r').read()
        self.data_path = os.path.normpath(path)

    def save(self, data):
        file = open(self.data_path, 'w')
        file.writelines(data)
        # print('data_saved')

    def load(self):
        file = open(self.data_path, 'r')
        return file.read()
