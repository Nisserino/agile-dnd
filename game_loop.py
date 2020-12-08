import cmd
from DungeonMaster import DungeonMaster


class Startup():
    def __init__(self, player, username, size, start):
        self.dm = DungeonMaster(size, player)
        self.dm.player.position = start
        self.username = username  # Might just dunk this var into entities
        self.start_loop()

    def start_loop(self):
        Bouncer(self.dm, self.username, 'move')


class Bouncer():
    def __init__(self, dm, username, action):
        self.dm = dm
        self.username = username
        self.check_action(action)

    def check_action(self, action):
        if action == 'move':
            GameLoop(self.dm, self.username).cmdloop()
        # Need to write combatloop to implement
        # elif action = 'combat':
        #     CombatLoop(self.dm, self.username).cmdloop()
        elif action == 'end':
            print('You died, noob')


# Rename to something more relevant
class GameLoop(cmd.Cmd):
    prompt = '-> '

    def __init__(self, dm, username):
        super().__init__()
        self.dm = dm
        self.username = username
        self.next_loop = 'combat'

    def do_hp(self, arg):
        'Check how much health points are left'
        print(f'You have {self.dm.player.endurance} hp left.')

    def do_north(self, arg):
        'Walk north'
        if self.check_move('North'):
            self.dm.player.move(0, -1)
            return True

    def do_south(self, arg):
        'Walk south'
        if self.check_move('South'):
            self.dm.player.move(0, 1)
            return True

    def do_west(self, arg):
        'Walk west'
        if self.check_move('West'):
            self.dm.player.move(1, -1)
            return True

    def do_east(self, arg):
        'Walk East'
        if self.check_move('East'):
            self.dm.player.move(1, 1)
            return True

    def do_directions(self, arg):
        'Check which directions you can walk in'
        print(self.dm.player.options)

    def do_give_up(self, arg):
        'Give up, and die in the dungeon'
        choice = input('Are you sure you give up? [Yes/No]\n -> ')
        return self.check_answer(choice)

#   - - - 'Unseen functions' - - -
    def check_answer(self, choice):
        if choice[0].lower() == 'y':
            self.next_loop = 'end'
            return True

    def update_move_options(self):
        self.dm.player.check_options()

    def check_move(self, choice):
        if choice not in self.dm.player.options:
            print('You can not walk that way.')
        else:
            return True

    def postcmd(self, stop, line):
        self.update_move_options()
        return cmd.Cmd.postcmd(self, stop, line)

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)  # change to 'combat' when made
