from mpv.view import View
from mpv.model import Model
from storage.storage import FileStorage
from storage.formatter import JsonFormatter


class Presenter:

    def __init__(self):
        self.view = View()
        self.model = Model(FileStorage(), JsonFormatter())
        self.view.set_presenter(self)

    def start(self):
        self.view.start()

    def add_note(self, note):
        self.model.add_note(note)

    def show_all_notes(self):
        return self.model.get_all_notes()

    def delete_note(self, note_id):
        self.model.delete_note(note_id)

    def edit_note(self, note_id, note):
        self.model.edit_note(note_id, note)

    def save_notes(self):
        self.model.save_notes_to_storage()

    def load_notes(self):
        self.model.load_notes_from_storage()

    def is_exist(self, note_id):
        return self.model.is_exist(note_id)
