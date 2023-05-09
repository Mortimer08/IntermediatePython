from notes.notebook import NoteBook
from notes.note import Note


class Model:
    def __init__(self, storage, formatter):
        self.storage = storage
        self.formatter = formatter
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

    def edit_note(self, note_id, note):
        self.note_book.replace(note_id, Note(note['header'], note['body']))

    def save_notes_to_storage(self):
        self.storage.save(self.formatter.to_serial(self.note_book))

    def load_notes_from_storage(self):
        data = self.storage.load()
        self.note_book = self.formatter.from_serial(data)

    def is_exist(self, id):
        return self.note_book.is_exist(id)
