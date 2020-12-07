import random

class Treasure:

    def __init__(self):
        self.treasures_rolled = []


    def treasure_randomizer(self):
        treasures = {
            'Lösa slantar': {40: 2},
            'Pengapung': {20: 6},
            'Guldsmycken': {15: 10},
            'Ädelsten': {10: 14},
            'Liten skattkista': {5: 20}
        }

        for i in treasures:
            for j, k in treasures[i].items():
                if random.randint(1, 100) <= j:
                    self.treasures_rolled.append([i, k])
        
        return self.treasures_rolled
