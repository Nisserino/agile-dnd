import entities
from treasure import Treasure
from gameboard import GameBoard
import random


class DungeonMaster:
    def __init__(self, size: int, player: entities.Entity):
        self.game_board = GameBoard()
        self.player = player
        self.enemies = [entities.Giantspider(), entities.Skeleton(), entities.Orc(), entities.Troll()]
        self.room_status = {}  # empty room {'pos': }, not empty room {'pos': (enemies, treasure)}

    def current_room(self, pos: list) -> tuple:
        if self.room_status[pos] != 'clear':
            return (True, self.print_room_status(pos))

        elif self.room_status[pos] == 'clear':
            return (False, 'Room is empty')

        else:
            self.entity_spawner(pos)
            return (True, self.print_room_status(pos))

    def entity_spawner(self, pos: list):
        enemies = []
        for e in self.enemies:
            npc = e()
            if random.randint(1, 100) <= npc.chance:
                enemies.append(npc)

        treasures = Treasure()
        self.room_status[pos] = (enemies, treasures)

    def print_room_status(self, pos: list) -> str:
        treasures = ', '.join(self.room_status[pos][1])
        enemies = ', '.join(self.room_status[pos][0])
        room = f'Enemies: {enemies}\nTreasurs: {treasures}'
        return room
