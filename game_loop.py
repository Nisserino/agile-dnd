import cmd
from DungeonMaster import DungeonMaster
# from combat_loop import CombatLoop


class Startup():
    def __init__(self, player, username, size, start):
        self.dm = DungeonMaster(size, player)
        self.dm.player.position = start
        self.dm.player.board_size = size
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
        elif action == 'combat':
            CombatLoop(self.dm, self.username).cmdloop()
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
        # self.dm.play_area.print_board()

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

#   - - - 'CMD functions' - - -
    def preloop(self):
        self.update_move_options()

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)  # change to 'combat' when made


class CombatLoop(cmd.Cmd):
    prompt = '-> '

    def __init__(self, dm, username):
        super().__init__()
        self.dm = dm
        self.username = username
        self.attack_order = []
        self.enemies = []
        self.next_loop = 'move'

    def do_attack(self, arg):
        'Attack, if there are more targets, you get to choose'
        pass

    def do_hp(self, arg):
        'Show the HP of everyone'
        pass

    def do_stats(self, arg):
        pass

    def do_escape(self, arg):
        'Attemt to run away from the fight'
        if self.escape():
            return True

#   - - - Unseen funcs - - -
    def deal_damage(self, attacker, blocker):
        if attacker.attack_roll() > blocker.evade_roll():
            blocker.take_hit()
            print(f'{attacker.name} landed a hit on {blocker.name}')
        else:
            print(f'{blocker.name} managed to evade the attack!')

    def init_rolls(self):
        pass

    def enemies_exist(self):
        # if self.dm.
        pass

    def escape(self):
        if self.dm.player.escape_roll():
            print('Managed to escape from the enemies')
            return True
        else:
            print('You slipped trying to run, and didn\'t manage to escape')

#   - - - Cmd specific funcs - - -
    def preloop(self):
        self.dm.entity_spawner(self.dm.player.position)

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)
