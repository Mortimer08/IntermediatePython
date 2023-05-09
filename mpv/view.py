from ui.main_menu import MainMenu
from ui.user_choice_checker import MMChoiceChecker as Checker


class View:
    def __init__(self):
        self.presenter = None
        self.main = MainMenu(self, 'Выберите номер команды:')
        self.keep_running = True
        self.check = Checker(self.main)

    def start(self):

        while self.keep_running:
            self.show_menu()
            choice = input()
            if self.check.check_choice(choice):
                self.main.run_menu_command(int(choice))
            else:
                print('Недопустимая команда')

    def set_presenter(self, presenter):
        self.presenter = presenter

    def show_menu(self):
        print(self.main.console_face())

    def add_note(self):
        note = {'header': input('Введите заголовок: '), 'body': input('Введите содержание: ')}
        self.presenter.add_note(note)
        print('Заметка добавлена')

    def show_all_notes(self):
        print('Содержимое записной книжки:\n')
        print(self.presenter.show_all_notes())

    def delete_note(self):
        user_choice = input('Введите ID заметки: ')
        if self.presenter.is_exist(user_choice):
            self.presenter.delete_note(user_choice)
            print(f'Заметка ID: {user_choice} удалена')
        else:
            print('Такой заметки нет')

    def edit_note(self):
        user_choice = input('Введите ID заметки: ')
        if self.presenter.is_exist(user_choice):
            note = {'header': input('Введите заголовок: '), 'body': input('Введите содержание: ')}
            self.presenter.edit_note(user_choice, note)
            print(f'Заметка ID: {user_choice} изменена')
        else:
            print('Такой заметки нет')

    def save_notes(self):
        self.presenter.save_notes()
        print('Записная книжка сохранена в файл')

    def load_notes(self):
        self.presenter.load_notes()
        print('Данные из файла загружены в записную книжку')

    def exit_command(self):
        print('Работа завершена')
        self.keep_running = False
