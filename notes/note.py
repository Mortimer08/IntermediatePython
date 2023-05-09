import datetime


class Note():
    # counter = 0

    def __init__(self, heading, body):
        # Note.counter += 1
        # self.id = str(Note.counter)
        self.date = f'{datetime.datetime.now():{"%Y-%m-%d %H:%M:%S"}}'
        self.set_heading(heading)
        self.set_body(body)

    # def set_ID(self, id):
    # self.id = id

    def set_date(self, date):
        self.date = date

    def set_heading(self, heading):
        self.heading = heading

    def set_body(self, body):
        self.body = body

    def show(self):
        note_face = '\n'
        # note_face += f'ID: {str(self.id)}'
        # note_face += '\n'
        note_face += f'Дата создания: {str(self.date)}'
        note_face += '\n'
        note_face += self.heading
        note_face += '\n'
        note_face += self.body
        return note_face
