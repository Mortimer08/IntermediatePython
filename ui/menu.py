
class Menu:

    def __init__(self, view, welcome):
        self.console_view = view
        self.commands_list = []
        self.items_count = 0
        self.set_welcome(welcome)

    def add_command(self, command):
        self.commands_list.append(command)
        self.items_count = len(self.commands_list)

    def console_face(self):
        console_face = self.welcome
        commands_count = 1
        console_face += "  "
        for command in self.commands_list:
            console_face += "  "
            console_face += commands_count
            commands_count += 1
            console_face += ". "
            console_face += command.description
            console_face += "  "
        return console_face

    def set_welcome(self, welcome):
        self.welcome = welcome

    def get_view(self):
        return self.console_view
