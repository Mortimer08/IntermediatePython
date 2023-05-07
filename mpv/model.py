class Model:
    def __init__(self):
        pass

    def add_note(self):
        print('model_add_note:')

    def get_all_notes(self):
        return 'model_get_all_notes'

    def delete_note(self, note_number):
        print(f'delete_note: {note_number}')

    def save_notes_to_storage(self):
        print('save_notes_to_storage')