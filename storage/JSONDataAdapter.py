import json
from notes.notebook import NoteBook
from notes.note import Note
class JSONDataAdapter:
    def to_json(data):
        return json.dumps(data, default=lambda x: x.__dict__)

    def from_json(data):
        try:
            target_note_book = NoteBook()
            json_note_book = json.loads(data)
            for note in json_note_book['notes_list'].values():
                target_note = Note(note['heading'], note['body'])
                target_note.set_ID(note['id'])
                target_note.set_date(note['date'])
                target_note_book.add(target_note)
            return target_note_book
        except AttributeError:
            print("Неверная структура файла")