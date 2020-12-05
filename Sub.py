import random
enemyAttackCount = 1 #temp variable

class Entity:
    def __init__(self, initiativ, endurance, attack, flexibility):
        self.initiativ = initiativ
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility

class Rider(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.lexibility = 4

    def blockAttack(self):
        self.x = enemyAttackCount - 1
        

class Wizard(Entity):
    def __init__(self):
        self.initiativ = 6
        self.endurance = 4
        self.attack = 9
        self.lexibility = 5

    def blindness(self):
        if random.randrange(0, 10) >= 8:
            print("Player escaped from room!")
        

class Thief(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.lexibility = 4

    def dubbelAward(self):
        if random.randint(1, 4) == 4:
            dungeonAward = dungeonAward * 2
            print(f"Player gets 2X COINS = {dungeonAward}") #How we'll handle taxes?
            
