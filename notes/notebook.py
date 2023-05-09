class NoteBook():
    id_queue = 1

    def __init__(self):
        self.notes_list = {}

    def show_all(self):
        notes_faces = ''
        for id in self.notes_list.keys():
            notes_faces += '-----------------'
            notes_faces += '\n'
            notes_faces += f'ID: {str(id)}'
            notes_faces += self.notes_list[id].show()
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
            print('Ошибка поиска заметки')

    def replace(self, note_id, note):
        try:
            self.notes_list[note_id] = note
        except:
            print('Ошибка поиска заметки')

    def add(self, note):
        self.notes_list[str(self.id_queue)] = note
        self.id_queue += 1

    def get(self, ID):
        print('returning_note_by_ID')

    def is_exist(self, id):
        return id in self.notes_list.keys()
