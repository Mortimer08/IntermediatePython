from ui.main_menu import MainMenu
from ui.user_choice_checker import MMChoiceChecker as checker

class View:
    def __init__(self):
        self.presenter = None
        self.main = MainMenu(self, 'Выберите номер команды:')
        self.keep_running = True
        self.check = checker(self.main)

    def start(self):

        while self.keep_running:
            self.show_menu()
            choice = input()
            if self.check.check_choice(choice):
                self.main.run_menu_command(int(choice))
            else:
                print('Недопустимая команда')
        # print('running_command_number_', command_number)
        # print('get_data_from_note_book')

    def set_presenter(self, presenter):
        self.presenter = presenter

    def show_menu(self):
        print(self.main.console_face())

    def add_note(self):
        self.presenter.add_note()

    def show_all_notes(self):
        print(self.presenter.show_all_notes())

    def delete_note(self):
        self.presenter.delete_note()

    def save_notes(self):
        self.presenter.save_notes()

    def exit_command(self):
        print('Работа завершена')
        self.keep_running = False