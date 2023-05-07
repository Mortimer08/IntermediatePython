from mpv.view import View
from mpv.model import Model
from storage.storage import FileStorage

class Presenter:

    def __init__(self):
        self.view = View()
        self.model = Model(FileStorage())
        self.view.set_presenter(self)

    def start(self):
        self.view.start()

    def add_note(self, note):
        self.model.add_note(note)

    def show_all_notes(self):
        return self.model.get_all_notes()

    def delete_note(self):
        self.model.delete_note(3)

    def save_notes(self):
        self.model.save_notes_to_storage()

    def load_notes(self):
        self.model.load_notes_from_storage()
