from dices import d6


class Entity():
    def __init__(self, initiativ, endurance, attack, flexibility):
        self.initiativ = initiativ
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.position = [0, 0]

    def attack_roll(self):
        # return attack roll
        return d6(attack)

    def evade_roll(self):
        # return evasion roll
        return d6(flexibility)

    def take_hit(self):
        # reduce HP by 1
        self.endurance -= 1

    def move(self):
        pass
