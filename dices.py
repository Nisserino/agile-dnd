import random


class Dice:

    def d6(self, rolls):
        # returns sum of rolls with d6 dices
        total_sum = 0
        for i in range(rolls):
            total_sum += random.randint(1, 6)
        return total_sum
