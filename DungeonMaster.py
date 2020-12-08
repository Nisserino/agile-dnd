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
        pass

    def npc_spawner(self):
        npcs = {}
        count = 0
        for e in self.enemies:
            if random.randint(1, 100) >= e.chance:
                count += 1  # Change with self.name when class is updated
                npc = e()
                npcs[count] = npc
        return npcs

    def item_spawner(self):
        pass

    def move_player(self):
        pass
