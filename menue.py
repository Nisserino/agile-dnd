import cmd


class Menue_loop(cmd.Cmd):
    intro = 'Welcome to the dungeon run!'
    prompt = '-> '

    def do_new_character(self, arg):
        'Start a new game with a new character'
        pass

    def do_load_character(self, arg):
        'Load an existing character'
        pass

    def do_start_game(self, arg):
        'Start the game'
        # call func to let player decide on board size
        pass

    def do_quit(self, arg):
        'Exit the game'
        return True


if __name__ == "__main__":
    Menue_loop().cmdloop()
