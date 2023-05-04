from ui.main_menu import MainMenu


class View:
    def __init__(self):
        self.main = MainMenu(self, 'Выберите номер команды:')

    def start(self):
        keep_running = True
        while keep_running:
            print(self.main.console_face())
            choice = input()
            print(choice)
            keep_running = False
        # print('view started')
        # print('show_main_menu')
        # command_number = input('awaiting_for_a_command: ')
        # print('running_command_number_', command_number)
        # print('get_data_from_note_book')
