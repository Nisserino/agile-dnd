import random

class Dices:

    def dice_sim(self, rolls):
        total_sum = 0

        for i in range(rolls):
            total_sum += random.randint(1, 6)
        return total_sum

