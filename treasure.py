import random


class Treasure:

    def __init__(self):
        self.treasures_rolled = []

    def treasure_randomizer(self):
        treasures = {
            'Coins': {40: 2},
            'Coin bag': {20: 6},
            'Jewlery': {15: 10},
            'Gems': {10: 14},
            'Treasure chest': {5: 20}
        }

        for i in treasures:
            for j, k in treasures[i].items():
                if random.randint(1, 100) <= j:
                    self.treasures_rolled.append([i, k])

        return self.treasures_rolled
