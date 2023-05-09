class MMChoiceChecker:

    def __init__(self, menu):
        self.menu = menu

    def check_choice(self, choice):
        result = False
        # print(len(self.menu.commands_list))
        if choice.isdigit():
            choice_int = int(choice)
            result = choice_int > 0 and choice_int <= len(self.menu.commands_list)
        return result
