

class Shop:

    def __init__(self, player, username):
        self.username = username
        self.player = player
        self.shop_items = {
            'Small potion': [50, 2],
            'Luck potion': [50, 1],
            'Armor': [100, 1],
            'Sword': [100, 1]
        }

    def checkout(self, amount, item, player_key):
        if self.check_item(item, player_key):
            return
        if self.check_money(amount, item):
            choice = input('Do you want to purchase this item? [Yes/No]\n ->')
            if self.check_choice(choice):
                print(f'{item} has been added to your inventory')
                return True
            else:
                print(f'{self.username} puts {item} back on the shelf')
        else:
            print('You dont have money, go do a run!')

    def check_money(self, amount, item):
        if amount >= self.shop_items[item][0]:
            return True

    def check_choice(self, choice):
        if choice[0].lower() == 'y':
            return True

    def check_item(self, item, player_key):
        if self.get_item(item) in self.player.inventory[player_key]:
            print('You can only buy this item once!')
            return True

    def get_item(self, item):
        return [item, self.shop_items[item][1]]
