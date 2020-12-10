from dices import Dices
import random


class Movement():
    def __init__(self):
        self.position = [0, 0]  # top left corner as base start pos
        self.board_size = 4  # Boardsize set to 4 as base value
        self.options = []

    def check_options(self):
        option = []
        # y
        if self.position[0] + 1 <= self.board_size - 1:  # position 0 indexed
            option.append('South')
        if self.position[0] - 1 >= 0:
            option.append('North')
        # x
        if self.position[1] + 1 <= self.board_size - 1:
            option.append('East')
        if self.position[1] - 1 >= 0:
            option.append('West')
        self.options = option

    def move(self, axle, direction):
        # Axle x or y (0 or 1), direction = 1 or -1
        self.position[axle] += direction


class Entity(Movement):
    # Contains character funcs such as attacking, aswell as holds the movement
    def __init__(self):
        super().__init__()
        self.gold = 0
        self.inventory = {
            'potions': [],
            'items': []
        }

    def attack_roll(self):
        # return attack roll
        return Dices.d6(self.attack)

    def evade_roll(self):
        # return evasion roll
        return Dices.d6(self.agility)

    def take_hit(self):
        # reduce HP by 1
        self.endurance -= 1

    def initiative_roll(self):
        # roll for initiative
        return Dices.d6(self.initiativ)

    def escape_roll(self):
        # Returns bool for escape attemt
        escape = False
        if random.randint(1, 10) <= self.agility:
            escape = True
        return escape


# Hero classes
class Knight(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Knight'
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.agility = 4


class Wizard(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Wizard'
        self.initiativ = 6
        self.endurance = 4
        self.attack = 9
        self.agility = 5


class Thief(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Thief'
        self.initiativ = 7
        self.endurance = 5
        self.attack = 5
        self.agility = 7


# Enemy classes
class Giantspider(Entity):
    def __init__(self):
        self.name = 'Giant spider'
        self.initiativ = 7
        self.endurance = 1
        self.attack = 2
        self.agility = 3
        self.chance = 20


class Skeleton(Entity):
    def __init__(self):
        self.name = 'Skeleton'
        self.initiativ = 4
        self.endurance = 2
        self.attack = 3
        self.agility = 3
        self.chance = 15


class Orc(Entity):
    def __init__(self):
        self.name = 'Orc'
        self.initiativ = 6
        self.endurance = 3
        self.attack = 4
        self.agility = 4
        self.chance = 10


class Troll(Entity):
    def __init__(self):
        self.name = 'Troll'
        self.initiativ = 2
        self.endurance = 4
        self.attack = 7
        self.agility = 2
        self.chance = 5
