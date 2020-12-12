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

    def enter_room(self) -> bool:
        room_dict = self.room_status[self.get_pos()]
        if room_dict['clear']:
            return False
        elif room_dict['exit']:
            pass
        elif room_dict['escape']:
            self.print_room_status
            return True
        else:
            self.entity_spawner()
            self.print_room_status()
            return True

    def leave_room(self, action):
        self.room_status[self.get_pos()][action] = True
        self.game_board.add_marker(
            self.player.position, self.get_marker(action))

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
        room_info = (
                f'Enemies: {enemies} \n'
                f'Treasures: {treasure}'
        )
        print(room_info)
