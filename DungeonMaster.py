import entities
from treasure import Treasure
from gameboard import GameBoard
from dices import Dices
import random


class DungeonMaster:
    def __init__(self, size, player):
        self.play_area = GameBoard.create_board(size)
        self.player = player
        self.enemies = [entities.Giantspider(), entities.Skeleton(), entities.Orc(), entities.Troll()]
        self.room_status = {}

    def current_room(self):
        enemies = self.npc_spawner()
        treasures = Treasure()

    def npc_spawner(self):
        npcs = {}
        for e in self.enemies:
            npc = e()
            if random.randint(1, 100) >= npc.chance:
                npcs[npc.name] = npc
        return npcs

    def move_player(self):
        pass
