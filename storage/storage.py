from notes.notebook import NoteBook
class Storage:
    def __init__(self):
        pass

    def save(self):
        print('data_saved')

    def load(self):
        print('data_loaded')
class FileStorage(Storage):
    def __init__(self):
        self.data_path = open('data/data_path.txt', 'r').read()
        self.note_book = NoteBook()

    def save(self):
        file = open(self.data_path, 'w+')
        file.writelines('data_saved')
        print('data_saved')

    def load(self):
        file = open(self.data_path, 'r')
        return file.read()