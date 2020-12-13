import cmd
from DungeonMaster import DungeonMaster
from roomdesc import RoomDescription
from end import End


class Startup():
    def __init__(self, player, username, size, start):
        player.position = start
        player.board_size = size
        self.dm = DungeonMaster(size, player)
        self.username = username
        self.start_loop()

    def start_loop(self):
        self.dm.leave_room('clear')
        Bouncer(self.dm, self.username, 'move')


class Bouncer():
    def __init__(self, dm, username, action):
        self.dm = dm
        self.username = username
        self.room_text = RoomDescription().get_description()
        self.place_marker('P')
        self.check_description()
        self.save_description()
        self.check_action(action)

    def check_description(self):
        description = self.dm.room_status[self.dm.get_pos()]['description']
        if description:
            self.room_text = description

    def save_description(self):
        self.dm.room_status[self.dm.get_pos()]['description'] = self.room_text

    def place_marker(self, marker):
        self.dm.game_board.add_marker(self.dm.player.position, marker)

    def check_action(self, action):
        if action == 'move':
            if self.dm.room_status[self.dm.get_pos()]['escape']:
                self.place_marker('E')
            MoveLoop(self.dm, self.username).cmdloop(self.room_text)
        elif action == 'combat':
            if self.spawn_checker():
                CombatLoop(self.dm, self.username).cmdloop(self.room_text)
            else:
                intro = 'No enemies in the room, phew!\n'
                MoveLoop(self.dm, self.username).cmdloop(
                    f'{intro + self.room_text}')
        elif action == 'end':
            End(self.dm.player, self.username)

    def spawn_checker(self):
        if self.dm.enter_room():
            if self.dm.room_status[
                    self.dm.get_pos()]['enemies']:
                return True


class MoveLoop(cmd.Cmd):
    prompt = '-> '

    def __init__(self, dm, username):
        super().__init__()
        self.dm = dm
        self.username = username
        self.next_loop = 'combat'
        self.dm.game_board.print_board()

    def do_hp(self, arg):
        'Check how much health points are left'
        print(f'You have {self.dm.player.endurance} hp left.')

    def do_gold(self, arg):
        'Check how much gold you have on you'
        print(f'You have {self.dm.player.gold} gold on your person')

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
        if choice:
            if choice[0].lower() == 'y':
                self.next_loop = 'end'
                self.dm.player.endurance = 0
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
        if not self.dm.room_status[self.dm.get_pos()]['escape']:
            self.dm.leave_room('clear')

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)


class CombatLoop(cmd.Cmd):
    prompt = '-> '

    def __init__(self, dm, username):
        super().__init__()
        self.dm = dm
        self.username = username
        self.attack_order = []
        self.enemies = []
        self.next_loop = 'move'
        self.turn = 0
        self.action_list = []

    def do_attack(self, arg):
        'Attack, if there are more targets, you get to choose'
        self.start_turn(True)
        if not self.enemies or self.dm.player.endurance <= 0:
            self.dm.leave_room('clear')
            return True

    def do_stats(self, arg):
        if self.attack_order:
            for entity in self.attack_order:
                self.get_stats(entity)

    def do_escape(self, arg):
        'Attemt to run away from the fight'
        if self.escape():
            self.dm.leave_room('escape')
            return True
        else:
            self.start_turn(False)  # Means player doesn't get to attack
            if not self.enemies or self.dm.player.endurance <= 0:
                return True

#   - - - Unseen funcs - - -
    def escape(self):
        if self.dm.player.escape_roll():
            print('Managed to escape from the enemies')
            return True
        else:
            print('You slipped trying to run.\nYou did not manage to escape.')

    def start_turn(self, attack):
        if attack:
            self.action_list.append([self.dm.player, self.enemies[0]])
        self.load_enemy_action()
        self.action_loop()
        self.turn += 1

#   - - - Display funcs - - -
    def get_stats(self, entity):
        print(
            f'{entity.name}\nHp: {entity.endurance}\n'
            f'Attack: {entity.attack}\nAgility: {entity.agility}\n'
        )

#   - - - Combat funcs - - -
    def action_loop(self):
        for entity in self.attack_order:
            for fight in self.action_list:
                if entity is fight[0]:
                    if fight[0].endurance <= 0:  # fight[0] == attacker obj
                        next
                    elif fight[1].name == 'Knight' and self.turn == 0:
                        print(
                            f'{fight[1]} managed to block the {fight[0]}s hit!'
                            )
                    else:
                        self.deal_damage(fight[0], fight[1])
        self.action_list = []

    def load_enemy_action(self):
        for entity in self.enemies:
            self.action_list.append([entity, self.dm.player])

    def deal_damage(self, attacker, blocker):
        if attacker.attack_roll() > blocker.evade_roll():
            blocker.take_hit()
            print(f'{attacker.name} landed a hit on the {blocker.name}')
            if attacker.name == 'Thief':
                if attacker.double_damage():
                    print('It was a critical hit!')
                    blocker.take_hit()
            self.death_check(blocker)
        else:
            print(f'{blocker.name} managed to evade the attack!')

    def death_check(self, entity):
        if entity.endurance <= 0:
            print(f'{entity.name} died.')
            if entity in self.enemies:
                self.attack_order.remove(entity)
                self.enemies.remove(entity)
            else:
                self.next_loop = 'end'

#   - - - Setup funcs - - -
    def init_rolls(self):
        self.attack_order.append([
            self.dm.player, self.dm.player.initiative_roll()])
        for enemy in self.enemies:
            self.attack_order.append([enemy, enemy.initiative_roll()])
        self.attack_order.sort(reverse=True, key=self.idx_one)
        self.order_cleanup()

    def populate_enemy_list(self):
        enemies = self.dm.room_status[self.dm.get_pos()]['enemies']
        for enemy in enemies:
            self.enemies.append(enemy)

    def idx_one(self, item):
        return item[1]

    def order_cleanup(self):
        clean_list = []
        for item in self.attack_order:
            clean_list.append(item[0])
        self.attack_order = clean_list

#   - - - Cmd specific funcs - - -
    def preloop(self):
        self.populate_enemy_list()
        self.init_rolls()

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)
