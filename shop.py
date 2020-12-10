import os


class Shop:

    def __init__(self, player):
        self.player = player
        self.inventory = []
        self.checkout_items = []
        self.available_items = {
            'Small potion': 10,
            'Big potion': 100,
            'Sword': 30,
            'Body Armor': 40
        }
        self.removed = [0, 0, 0, 0]
        self.s_potion = 2
        self.b_potion = 100
        self.sword = 1
        self.armor = 1

    def menu(self):
        menu = {}
        menu['1'] = 'Small potion'
        menu['2'] = 'Big potion'
        menu['3'] = 'Sword'
        menu['4'] = 'Body Armor'
        menu['5'] = 'Available items'
        menu['6'] = 'Go to checkout'

        alternative = menu.keys()
        for i in alternative:
            print(i, menu[i], sep=". ")
        print()

    def shop_loop(self):
        pass

    def checkout(self):
        os.system('cls')
        total_amount = 0
        for i in self.checkout_items:
            for j in i:
                total_amount += j
                # gold -= j
        print('You total amount is: ' + str(total_amount))
        print(self.inventory)
        # return self.inventory ?

    def remove_item(self):
        pass
