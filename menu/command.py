class command():
    def __init__(self,menu,description):
        self.menu = menu
        self.description = description

    def run_command(self):
        print('run_command')

class add_note (command):
    def __init__(self, menu, description='Добавить заметку'):
        command.__init__(self, menu, description='Добавить заметку')

    def run_command(self):
        print('run_command_add_note')