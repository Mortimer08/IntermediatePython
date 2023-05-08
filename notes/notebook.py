class NoteBook():
    def __init__(self):
        self.notes_list = {}

    def show_all(self):
        notes_faces = ''
        for note in self.notes_list.values():
            notes_faces += '-----------------'
            notes_faces += note.show()
            notes_faces += '\n'
            notes_faces += '-----------------'
            notes_faces += '\n'
        return notes_faces

    def show_younger(self, date):
        print('show_notes_younger_than_defined_date')

    def delete(self, note_id):
        try:
            self.notes_list.pop(note_id)
        except:
            print('Такой заметки нет')

    def add(self, note):
        self.notes_list[note.id] = note
        # print('notebook_adding_note')


    def get(self, ID):
        print('returning_note_by_ID')
