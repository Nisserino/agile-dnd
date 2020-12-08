import cmd
from DungeonMaster import DungeonMaster

"""
create class that starts up dungeon master, and is able to send it on
this in order to keep DM alive thoroughout the game
so that we can save all relevant player info between movement and combat
"""


class Bouncer():
    def __init__(self, player, username, size, start, dm):
        self.dm = DungeonMaster(size, player)
        self.dm.player.position = start
        self.username = username  # Might just dunk this var into entities
        self.test()

    def test(self):
        GameLoop(4, player, username)


class GameLoop(cmd.Cmd):
    intro = ''
    prompt = '-> '

    def __init__(self, size, player, username):
        super().__init__()
        self.username = username.title()
        self.dm = DungeonMaster(size, player)
        self.dm.player.board_size = size
        self.update_move_options()
        self.intro = f'Welcome, brave {self.username} to the dungeon!'

    def do_hp(self, arg):
        'Check how much health points are left'
        print(f'You have {self.dm.player.endurance} hp left.')

    # debug func
    def do_check_pos(self, arg):
        print(self.dm.player.position)
        print(self.dm.player.board_size)

    def do_north(self, arg):
        'Walk north'
        if self.check_move('North'):
            self.dm.player.move(0, -1)

    def do_south(self, arg):
        'Walk south'
        if self.check_move('South'):
            self.dm.player.move(0, 1)

    def do_west(self, arg):
        'Walk west'
        if self.check_move('West'):
            self.dm.player.move(1, -1)

    def do_east(self, arg):
        'Walk East'
        if self.check_move('East'):
            self.dm.player.move(1, 1)

    def do_directions(self, arg):
        'Check which directions you can walk in'
        print(self.dm.player.options)

    def do_give_up(self, arg):
        'Give up, and die in the dungeon'
        choice = input('Are you sure you give up?\n -> ')
        return self.check_answer(choice)

#   - - - 'Unseen functions' - - -
    def update_move_options(self):
        self.dm.player.check_options()

    def check_move(self, choice):
        if choice not in self.dm.player.options:
            print('You can not walk that way.')
        else:
            return True

    def postcmd(self, stop, line):
        self.update_move_options()


# Testing, to be removed
import entities as e
player = e.Thief()
username = 'Persan'
GameLoop(4, player, username).cmdloop()
