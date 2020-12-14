import cmd
from shop import Shop


class ShopLoop(cmd.Cmd):

    prompt = '-> '

    def __init__(self, player, username):
        super().__init__()
        self.intro = f'Welcome to D&D shop {username}!'
        self.player = player
        self.username = username
        self.shop = Shop(player, username)

    def do_small_potion(self, args):
        "Cost: 75 gold, heals 2"
        if self.shop.checkout(self.player.gold, 'Small potion', 'potions'):
            self.add_inventory('potions', self.shop.get_item('Small potion'))

    def do_smaller_potion(self, args):
        "Cost: 50 gold, heals 1"
        if self.shop.checkout(self.player.gold, 'Smaller potion', 'potions'):
            self.add_inventory('potions', self.shop.get_item('Smaller potion'))

    def do_armor(self, args):
        "Cost: 100 gold, adds 1 to endurance"
        if self.shop.checkout(self.player.gold, 'Armor', 'items'):
            self.add_inventory('items', self.shop.get_item('Armor'))

    def do_sword(self, args):
        "Cost: 100 gold, adds 1 to attack"
        if self.shop.checkout(self.player.gold, 'Sword', 'items'):
            self.add_inventory('items', self.shop.get_item('Sword'))

    def do_gold(self, args):
        "See how much gold you have"
        print('You have: ' + str(self.player.gold) + ' gold!')

    def do_quit(self, args):
        "Exit shop"
        return True

    def add_inventory(self, key, item):
        self.player.gold -= self.shop.shop_items[item[0]][0]
        self.player.inventory[key].append(item)

    def activate_items(self):
        for item in self.player.inventory['potions']:
            self.player.endurance += item[1]
        for item in self.player.inventory['items']:
            if item[0] == 'Sword':
                self.player.attack += item[1]
            elif item[0] == 'Armor':
                self.player.endurance += item[1]

    def wipe_item_stats(self):
        potions = []
        items = []
        for key in self.player.inventory:
            for item in self.player.inventory[key]:
                if key == 'potions':
                    potions.append([item[0], 0])
                else:
                    items.append([item[0], 0])
        self.player.inventory['potions'] = potions
        self.player.inventory['items'] = items

    def postloop(self):
        self.activate_items()
        self.wipe_item_stats()
