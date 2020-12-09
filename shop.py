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
        shopping = True
        self.menu()
        while shopping:
            option = int(input(
                'Enter a number of the item you want to purchase: '
            ))
            if option >= 5:
                if option == 5:
                    self.menu()
                elif option == 6:
                    shopping = False
                    self.checkout()
                else:
                    print('That item is not available')
            elif self.removed[option-1] == 1:
                print("""
                This item is already in your inventory.
                You can only purchase this item once a run.
                """)
            elif option == 1:
                print('Small potion is ready for checkout!')
                print()
                self.checkout_items.append(
                    [self.available_items.get('Small potion')])
                self.inventory.append(['Small potion', self.s_potion])
            elif option == 2:
                print('Big potion is ready for checkout!')
                print()
                self.removed[1] += 1
                self.checkout_items.append(
                    [self.available_items.get('Big potion')]
                )
                del self.available_items['Big potion']
                self.inventory.append(['Big potion', self.b_potion])
            elif option == 3:
                print('Sword is ready for checkout!')
                print()
                self.removed[2] += 1
                self.checkout_items.append(
                    [self.available_items.get('Sword')]
                )
                del self.available_items['Sword']
                self.inventory.append(['Sword', self.sword])
            elif option == 4:
                print('Body Armor is ready for checkout!')
                print()
                self.removed[3] += 1
                self.checkout_items.append(
                    [self.available_items.get('Body Armor')]
                )
                del self.available_items['Body Armor']
                self.inventory.append(['Body Armor', self.armor])

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


shop = Shop('player1')
shop.shop_loop()
