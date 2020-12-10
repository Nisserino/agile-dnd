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

    def populate_rooms(self, size):
        for num in range(size):
            self.room_status[f'{num}'] = {
                'clear': False,
                'enemies': [],
                'treasure': [],
                'exit': False
            }

    def get_pos(self):
        pos = 0
        coords = self.player.position
        pos += coords[0] * self.player.board_size + coords[1]
        return f'{pos}'

    def enter_room(self) -> bool:
        if self.room_status[self.get_pos()]['clear']:
            return False
        else:
            self.entity_spawner(self.get_pos)
            self.print_room_status()
            return True

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
        enemies = ', '.join(room_status['enemies'])
        treasure = ', '.join(room_status['treasure'])
        room_info = (
                f'Enemies: {enemies} \n'
                f'Treasures: {treasure}'
        )
        print(room_info)
