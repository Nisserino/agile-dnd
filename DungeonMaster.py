import entities
from treasure import Treasure
from gameboard import GameBoard
from dices import Dices
import random


class DungeonMaster:
    def __init__(self, size: int, player: entities.Entity):
        self.play_area = GameBoard.create_board(size)
        self.player = player
        self.enemies = [entities.Giantspider(), entities.Skeleton(), entities.Orc(), entities.Troll()]
        self.room_status = {}  # empty room {'pos': }, not empty room {'pos': (enemies, treasure)}

    def current_room(self, pos: list):
        if self.room_status[pos] != 'clear':
            enemies = self.room_status[pos][0]
            treasures = self.room_status[pos][1]
            return (True, [i for i in treasures])

        elif self.room_status[pos] == 'clear':
            return 'Room is empty'
        else:
            enemies = self.npc_spawner()
            treasures = Treasure()
            return (enemies, treasures)

    def entity_spawner(self, pos):
        enemies = []
        for e in self.enemies:
            npc = e()
            if random.randint(1, 100) <= npc.chance:
                enemies.append(npc)

        treasures = Treasure()
        self.room_status[pos] = (enemies, treasures)

    def combat(self):
        pass

    def print_room_status(self, treasures: list, enemies: list):
        pass
