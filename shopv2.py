import entities


class Shop:

    def __init__(self, player):
        self.shop_items = {
            'Small potion': 10,
            'Luck potion': 30,
            'Armor': 40,
            'Sword': 40
        }
        self.small_potion = 2
        self.luck_potion = ['Luck potion', 1]
        self.armor = ['Armor', 1]
        self.sword = ['Sword', 1]

    def check_money(self, amount, item):
        if amount >= self.shop_items[item]:
            return True

    def checkout(self, amount, item):
        if self.check_money(amount, item):
            do = True
            while do:
                sure = input(f'Do you want to buy {item}? yes/no: ').lower()
                if sure == 'yes':
                    print(item + ' has been added to your inventory!')
                    return True
                    do = False
                elif sure == 'no':
                    print(item + ' has been removed, choose another item.')
                    return False
                    do = False
                else:
                    print('Only yes or no.')
        else:
            print('You dont have money, go do a run!')
