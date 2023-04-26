class note_book():
    def __init__(self):
        self.notes_list=[]
    def show_all(self):
        print('show_all_notes')

    def show_younger(self,date):
        print('show_notes_younger_than_defined_date')

    def delete(self,note):
        print('deleting_note')

    def add(self,note):
        print('additing_note')

    def get(self,ID):
        print('returning_note_by_ID')

