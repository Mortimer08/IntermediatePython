from notes.notebook import NoteBook
from notes.note import Note
from storage.JSONDataAdapter import JSONDataAdapter
class Model:
    def __init__(self, storage):
        self.storage = storage
        self.note_book = NoteBook()

    def add_note(self, note):
        self.note_book.add(Note(note['header'], note['body']))
        # print('model_add_note: ')

    def get_all_notes(self):
        return self.note_book.show_all()

    def load_notes(self):
        self.storage.load()

    def delete_note(self, note_id):
        self.note_book.delete(note_id)

    def save_notes_to_storage(self):
        self.storage.save(JSONDataAdapter.to_json(self.note_book))

    def load_notes_from_storage(self):
        data = self.storage.load()
        #print(data)
        self.note_book = JSONDataAdapter.from_json(data)