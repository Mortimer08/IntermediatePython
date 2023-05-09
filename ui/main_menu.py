from ui.menu import Menu
import ui.command as cmd


class MainMenu(Menu):
    def __init__(self, view, welcome):
        Menu.__init__(self, view, welcome)
        Menu.add_command(self, cmd.AddNote(self))
        Menu.add_command(self, cmd.ShowAllNotes(self))
        Menu.add_command(self, cmd.DeleteNote(self))
        Menu.add_command(self, cmd.EditNote(self))
        Menu.add_command(self, cmd.SaveNotes(self))
        Menu.add_command(self, cmd.LoadNotes(self))
        Menu.add_command(self, cmd.ExitCommand(self))
