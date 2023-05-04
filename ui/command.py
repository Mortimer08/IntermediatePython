class Command:
    def __init__(self,menu,description):
        self.menu = menu
        self.description = description

    def run_command(self):
        print('run_command')

class add_note (Command):
    def __init__(self, menu, description='Добавить заметку'):
        Command.__init__(self, menu, description)

    def run_command(self):
        print('run_command_add_note')

class show_all_notes (Command):
    def __init__(self, menu, description='Показать все заметки'):
        Command.__init__(self, menu, description)

    def run_command(self):
        print('run_show_all_notes')