class Entity:
pass

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