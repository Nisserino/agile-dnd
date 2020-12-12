import cmd
from ChCreation import CharacterCreation as CC
import saveLoad as SL
import game_loop


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
        'load_character <name>\n' \
            'If no match, saved characternames will be printed'
        if arg in self.data_handler.get_names():
            self.character = [
                self.data_handler.load_character(arg), arg]
        else:
            self.do_see_characters('')  # empty string to supplement 'arg'

    def do_start_game(self, arg):
        'Start the game'
        if self.character:
            PickBoardSize(self.character[0], self.character[1]).cmdloop()
        else:
            print('You need to load a character before you can start playing')

    def do_check_load(self, arg):
        'See what character is loaded'
        if self.character:
            print(f'Name: {self.character[1]}\nHero: {self.character[0].name}')
        else:
            print('You have not loaded a character yet.')

    def do_see_characters(self, arg):
        'See what characters exist'
        characters = self.data_handler.get_names()
        if characters:
            print(', '.join(characters))
        else:
            print(
                'No saved characters yet\nUse command new_character '
                'to create one!')

    def do_quit(self, arg):
        'Exit the game'
        return True  # Exits the loop

    def postloop(self):
        self.data_handler.update(tuple(self.character))
        self.data_handler.file_handler.save(
            self.data_handler.character_data
        )


class PickBoardSize(cmd.Cmd):
    intro = 'Pick a boardsize'
    prompt = '-> '

    def __init__(self, player, username):
        super().__init__()
        self.board_size = 0
        self.player = player
        self.username = username

    def do_small(self, arg):
        'Play with a board that is 4x4 tiles big'
        self.board_size = 4
        return True

    def do_medium(self, arg):
        'Play with a board that is 5x5 tiles big'
        self.board_size = 5
        return True

    def do_big(self, arg):
        'Play with a board that is 8x8 tiles big'
        self.board_size = 8
        return True

    def postloop(self):
        PickStart(self.player, self.username, self.board_size).cmdloop()


class PickStart(cmd.Cmd):
    intro = 'Pick your starting corner of the map'
    prompt = '-> '

    def __init__(self, player, username, board_size):
        super().__init__()
        self.player = player
        self.username = username
        self.board_size = board_size
        self.start = []

    def do_north_west(self, arg):
        'Start in the top left corner of the map'
        self.start = [0, 0]
        return True

    def do_north_east(self, arg):
        'Start in the top right corner of the map'
        self.start = [0, self.board_size - 1]
        return True

    def do_south_west(self, arg):
        'Start in the bottom left corner of the map'
        self.start = [self.board_size - 1, 0]
        return True

    def do_south_east(self, arg):
        'Start in the bottom right corner of the map'
        self.start = [self.board_size - 1, self.board_size - 1]
        return True

    def postloop(self):
        game_loop.Startup(
            self.player, self.username, self.board_size, self.start)


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
            self.data_handler.update(CC(user, 'Wizard').send_to_save())
            return True

    def do_knight(self, arg):
        'Create a knight'
        user = self.get_username()
        if user:
            self.data_handler.update(CC(user, 'Knight').send_to_save())
            return True

    def do_theif(self, arg):
        'Create a thief'
        user = self.get_username()
        if user:
            self.data_handler.update(CC(user, 'Thief').send_to_save())
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
