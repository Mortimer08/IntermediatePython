import json
from notes.notebook import NoteBook
from notes.note import Note

class Formatter:
    def to_serial(self):
        pass
    def from_serial(self):
        pass
class JsonFormatter(Formatter):
    def to_serial(self, data):
        return json.dumps(data, default=lambda x: x.__dict__)

    def from_serial(self, data):
        try:
            target_note_book = NoteBook()
            json_note_book = json.loads(data)
            for id in json_note_book['notes_list'].keys():
                json_note = json_note_book['notes_list'][id]
                target_note = Note(json_note['heading'], json_note['body'])
                target_note.set_date(json_note['date'])
                target_note_book.add(target_note)
            return target_note_book
        except AttributeError:
            print("Неверная структура файла")
