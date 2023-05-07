import datetime


class note():
    counter = 0

    def __init__(self, heading, body):
        note.counter += 1
        self.id = note.counter
        self.date = datetime.datetime.now()
        self.set_heading(heading)
        self.set_body(body)

    def set_heading(self, heading):
        self.heading = heading

    def set_body(self, body):
        self.body = body

    def show(self):
        print(self.id)
        print(self.heading)
        print(self.body)
