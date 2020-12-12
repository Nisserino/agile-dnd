import cmd
from ChCreation import CharacterCreation as CC
import saveLoad as SL


class Menue_loop(cmd.Cmd):
    intro = 'Welcome to the dungeon run!'
    prompt = '-> '

    def __init__(self):
        super().__init__()
        self.data_handler = SL.DataHandler()
        self.character = []

    def do_new_character(self, arg):
        'Create a new character'
        CharacterCreationLoop(self.data_handler).cmdloop()

    def do_load_character(self, arg):
        'Load an existing character'
        pass  # Add func call when class is ready

    def do_start_game(self, arg):
        'Start the game'
        if self.character:
            pass
        else:
            print('You need to load a character before you can start playing')

    def do_check_load(self, arg):
        'See what character is loaded'
        if self.character:
            print(f'Name: {self.character[0]}\nHero: {self.character.name}')
        else:
            print('You have not loaded a character yet.')

    def do_quit(self, arg):
        'Exit the game'
        return True  # Exits the loop


class CharacterCreationLoop(cmd.Cmd):
    intro = 'What would you like to play as?'
    prompt = '-> '

    def __init__(self, data_handler):
        super().__init__()
        self.data_handler = data_handler
        self.taken_names = self.data_handler.get_names()

    def do_wizard(self, arg):
        'Create a wizard'
        user = self.get_username()
        if user:
            self.data_handler.update(CC('Wizard', user))
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
        username = input('What are you called?\n-> ')
        check = self.check_username(username)
        if check:
            return username
        else:
            return False

    def check_username(self, username):
        if username in self.taken_names:
            print('That username is already taken!')
        else:
            return username

    def postloop(self):
        self.data_handler.file_handler.save(
            self.data_handler.character_data)


if __name__ == "__main__":
    Menue_loop().cmdloop()
