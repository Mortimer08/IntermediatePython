from mpv.view import View
from  mpv.model import Model

class Presenter:

    def __init__(self):
        self.view = View()
        self.model = Model()
        self.view.set_presenter(self)

    def start(self):
        self.view.start()

    def add_note(self):
        self.model.add_note()

    def show_all_notes(self):
        return self.model.get_all_notes()

    def delete_note(self):
        self.model.delete_note(3)

    def save_notes(self):
        self.model.save_notes_to_storage()
