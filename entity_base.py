from dices import d6
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
        return d6(self.attack)

    def evade_roll(self):
        # return evasion roll
        return d6(self.flexibility)

    def take_hit(self):
        # reduce HP by 1
        self.endurance -= 1

    def initiative_roll(self):
        # roll for initiative
        return d6(self.initiativ)

    def escape_roll(self):
        # Returns bool for escape attemt
        escape = False
        if random.randint(1, 10) <= self.flexibility:
            escape = True
        return escape

    def move(self):
        pass
