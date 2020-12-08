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

    def current_room(self, pos: list, status: dict):
        if status[pos]:
            enemies = status[pos][0]
            treasures = status[pos][1]

        else:
            enemies = self.npc_spawner()
            treasures = Treasure()

        return (enemies, treasures)

    def npc_spawner(self):
        npcs = []
        for e in self.enemies:
            npc = e()
            if random.randint(1, 100) <= npc.chance:
                npcs.append(npc)
        return npcs

    def combat(self):
        pass
