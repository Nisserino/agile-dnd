import cmd


class Menue_loop(cmd.Cmd):
    intro = 'Welcome to the dungeon run!'
    prompt = '-> '

    def do_new_game(self, arg):
        'Start a new game with a new character'
        pass

    def do_load_game(self, arg):
        'Load an existing character'
        pass

    def do_quit(self, arg):
        'Exit the game'
        return True


if __name__ == "__main__":
    Menue_loop().cmdloop()
