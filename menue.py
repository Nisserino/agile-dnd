import cmd
from ChCreation import CharacterCreation as CC


class Menue_loop(cmd.Cmd):
    intro = 'Welcome to the dungeon run!'
    prompt = '-> '

    def do_new_character(self, arg):
        'Create a new character'
        CharacterCreationLoop().cmdloop()

    def do_load_character(self, arg):
        'Load an existing character'
        pass  # Add func call when class is ready

    def do_start_game(self, arg):
        'Start the game'
        # call func to let player decide on board size
        pass

    def do_quit(self, arg):
        'Exit the game'
        return True  # Exits the loop


class CharacterCreationLoop(cmd.Cmd):
    intro = 'What would you like to play as?'
    prompt = '-> '

    def __init__(self):
        super().__init__()
        self.taken_names = ('pelle')  # test name, will get replaced

    def do_wizard(self, arg):
        'Create a wizard'
        user = self.get_username()
        if user:
            CC('Wizard', user)
            return True

    def do_knight(self, arg):
        'Create a knight'
        user = self.get_username()
        if user:
            CC('Knight', user)
            return True

    def do_theif(self, arg):
        'Create a thief'
        user = self.get_username()
        if user:
            CC('Knight', user)
            return True

    def get_username(self):
        username = input('What are you called?')
        check = self.check_username(username)
        if check:
            return username
        else:
            return False

    def check_username(self, username):
        if username in self.taken_names:
            print('That username is already taken!')


if __name__ == "__main__":
    Menue_loop().cmdloop()
