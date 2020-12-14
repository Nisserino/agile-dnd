import entities
from treasure import Treasure
from gameboard import GameBoard
import random


class DungeonMaster:
    def __init__(self, size: int, player: entities.Entity):
        self.game_board = GameBoard(size)
        self.player = player
        self.enemies = [
            entities.Giantspider, entities.Skeleton,
            entities.Orc, entities.Troll]
        self.room_status = {}
        self.populate_room_status_dict(size)
        self.place_exit()

    def populate_room_status_dict(self, size):
        for num in range(size*size):
            self.room_status[f'{num}'] = {
                'clear': False,
                'enemies': [],
                'treasure': [],
                'exit': False,
                'escape': False,
                'description': ''
            }

    def get_pos(self):
        pos = 0
        coords = self.player.position
        pos += coords[0] * self.player.board_size + coords[1]
        return f'{pos}'

    def place_exit(self):
        player = self.player.position
        size = self.player.board_size
        exit_ref = []
        for coord in player:
            if coord == 0:
                exit_ref.append(size - (1 + random.randint(0, size//2)))
            else:
                exit_ref.append(random.randint(0, size//2))
        pos = 0
        pos += exit_ref[0] * size + exit_ref[1]
        self.room_status[f'{pos}']['exit'] = True

    def enter_room(self) -> bool:
        room_dict = self.room_status[self.get_pos()]
        if room_dict['exit']:
            print('This is the exit')
        elif room_dict['clear']:
            return False
        elif room_dict['escape']:
            self.print_room_status()
            return True
        else:
            self.entity_spawner()
            self.print_room_status()
            return True

    def leave_room(self, action):
        self.room_status[self.get_pos()][action] = True
        self.game_board.add_marker(
            self.player.position, self.get_marker(action))
        if action == 'clear' and self.player.endurance >= 1:
            for treasure in self.room_status[self.get_pos()]['treasure']:
                self.player.gold += treasure[1]
            self.room_status[self.get_pos()]['treasure'] = []

    def get_marker(self, action):
        markers = {
            'clear': 'C',
            'escape': 'R',
            'exit': 'E'
        }
        return markers[action]

    def entity_spawner(self):
        pos = self.get_pos()
        if not self.room_status[pos]['clear'] and \
           not self.room_status[pos]['enemies']:
            enemies = []
            for e in self.enemies:
                npc = e()
                if random.randint(1, 100) <= npc.chance:
                    enemies.append(npc)

            treasures = Treasure().treasure_randomizer()
            self.room_status[pos]['enemies'] = enemies
            self.room_status[pos]['treasure'] = treasures

    def print_room_status(self) -> str:
        room_status = self.room_status[self.get_pos()]
        enemies = room_status['enemies']
        treasure = room_status['treasure']
        self.print_treasure_enemies(enemies, treasure)

    def print_treasure_enemies(self, enemies, treasure):
        if len(enemies) == 0:
            found_enemies = 'No enemies found\n'
        else:
            found_enemies = ''
            for enemy in enemies:
                found_enemies += enemy.name + '\n'
        if len(treasure) == 0:
            found_treasure = 'No treasure found\n'
        else:
            found_treasure = ''
            for treasures in treasure:
                found_treasure += treasures[0] + ' ' + str(treasures[1]) + '\n'
        room_info = (
            f'Enemies:\n{found_enemies} \n'
            f'Treasures:\n{found_treasure}'
        )
        print(room_info)
