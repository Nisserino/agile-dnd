import random


class Entity:
    def __init__(self, initiativ, endurance, attack, flexibility, heroType):
        self.initiativ = initiativ
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.heroType = ''


class Knight(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.lexibility = 4
        self.heroType ='Knight'

    def blockAttack(self):
        pass #return combat loop/ The Knight has first fist always
        

class Wizard(Entity):
    def __init__(self):
        self.initiativ = 6
        self.endurance = 4
        self.attack = 9
        self.lexibility = 5
        self.heroType ='Wizard'

    def blindness(self):
        if random.randrange(0, 100) <= 80:
            print("Player escaped from room!")
        

class Thief(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.lexibility = 4
        self.heroType ='Thief'

    def dubbelAward(self):
        if random.randint(1, 4) == 4:
            Treasure.treasures = Treasure.treasures * 2
            print(f"Player gets 2X COINS = {Treasure.treasures}")