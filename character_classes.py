from dices import Dices
import random


class Entity():
    def __init__(self, initiativ, endurance, attack, flexibility):
        self.initiativ = initiativ
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.position = [0, 0]
        self.board_size = 0

    def attack_roll(self):
        # return attack roll
        return Dices.d6(self.attack)

    def evade_roll(self):
        # return evasion roll
        return Dices.d6(self.flexibility)

    def take_hit(self):
        # reduce HP by 1
        self.endurance -= 1

    def initiative_roll(self):
        # roll for initiative
        return Dices.d6(self.initiativ)

    def escape_roll(self):
        # Returns bool for escape attemt
        escape = False
        if random.randint(1, 10) <= self.flexibility:
            escape = True
        return escape

    def move(self):
        pass


# Hero classes
class Rider(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.flexibility = 4


class Wizard(Entity):
    def __init__(self):
        self.initiativ = 6
        self.endurance = 4
        self.attack = 9
        self.flexibility = 5


class Thief(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.flexibility = 4


# Enemy classes
class Giantspider(Entity):
    def __init__(self):
        self.initiativ = 7
        self.endurance = 9
        self.attack = 2
        self.flexibility = 3


class Skeleton(Entity):
    def __init__(self):
        self.initiativ = 4
        self.endurance = 2
        self.attack = 3
        self.flexibility = 3


class Orc(Entity):
    def __init__(self):
        self.initiativ = 6
        self.endurance = 3
        self.attack = 4
        self.flexibility = 4


class Troll(Entity):
    def __init__(self):
        self.initiativ = 2
        self.endurance = 4
        self.attack = 7
        self.flexibility = 2
