import cmd


class Menue_loop(cmd.Cmd):
    intro = 'Welcome to the dungeon run!'
    prompt = '-> '

    def do_new_character(self, arg):
        'Start a new game with a new character'
        pass  # add func call when class is ready

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


if __name__ == "__main__":
    Menue_loop().cmdloop()
