class Command:
    def __init__(self, menu, description):
        self.menu = menu
        self.description = description

    def run_command(self):
        print('run_command')


class AddNote(Command):
    def __init__(self, menu):
        Command.__init__(self, menu, 'Добавить заметку')

    def run_command(self):
        self.menu.get_view().add_note()


class ShowAllNotes(Command):
    def __init__(self, menu, description='Показать все заметки'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().show_all_notes()


class DeleteNote(Command):
    def __init__(self, menu, description='Удалить заметку'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().delete_note()


class EditNote(Command):
    def __init__(self, menu, description='Редактировать заметку'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().edit_note()


class SaveNotes(Command):
    def __init__(self, menu, description='Сохранить заметки'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().save_notes()


class LoadNotes(Command):
    def __init__(self, menu, description='Загрузить заметки'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().load_notes()


class ExitCommand(Command):
    def __init__(self, menu, description='Выход'):
        Command.__init__(self, menu, description)

    def run_command(self):
        self.menu.get_view().exit_command()
