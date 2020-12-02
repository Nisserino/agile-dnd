import random
enemyAttackCount = 1 #temp variable


#class Ability():
#    def __init__(self, blindness, block, dubbelSkatt):
#        self.blindness = blindness
#        self.block = block
#        self.dubbelSkatt = dubbelSkatt


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
        if random.randrange(0, 1) <= 0.8:
            return "escape"
        

class Thief(Entity):
    def __init__(self):
        self.initiativ = 5
        self.endurance = 9
        self.attack = 6
        self.lexibility = 4

    def dubbelAward(self):
        if random.randint(1, 4) == 4:
            return "dubble award"
            
 

#Rider = Heroes(5, 9, 6, 4, "Block first attack")
#Wizard = Heroes(6, 4, 9, 5, "Blind 80%")
#Tjuven = Heroes(7, 5, 5, 7, "%20 chans to more skatt")

#HeroList = []