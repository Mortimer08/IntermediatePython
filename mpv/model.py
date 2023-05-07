from notes.notebook import NoteBook
from notes.note import Note
import json
class Model:
    def __init__(self, storage):
        self.storage = storage
        self.note_book = NoteBook()

    def add_note(self, note):
        self.note_book.add(Note(note['header'], note['body']))
        print('model_add_note: ')

    def get_all_notes(self):
        return self.note_book.show_all()

    def load_notes(self):
        self.storage.load()

    def delete_note(self, note_number):
        print(f'delete_note: {note_number}')

    def save_notes_to_storage(self):
        print(json.dumps(self.note_book))
        self.storage.save()

    def load_notes_from_storage(self):

        self.storage.load()