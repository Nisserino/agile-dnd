import cmd
from shopv2 import Shop


class Shop_loop(cmd.Cmd):

    prompt = '->'

    def __init__(self, player, username):
        super().__init__()
        self.intro = f'Welcome to D&D shop {username}!'
        self.player = player
        self.username = username
        self.shop = Shop(player, username)

    def do_small_potion(self, args):
        "Cost: 50 gold"
        if self.shop.checkout(self.player.gold, 'Small potion', 'potions'):
            self.add_inventory('potions', self.shop.get_item('Small potion'))

    def do_luck_potion(self, args):
        "Cost: 50 gold"
        if self.shop.checkout(self.player.gold, 'Luck potion', 'potions'):
            self.add_inventory('potions', self.shop.get_item('Luck potion'))

    def do_armor(self, args):
        "Cost: 100 gold"
        if self.shop.checkout(self.player.gold, 'Armor', 'items'):
            self.add_inventory('items', self.shop.get_item('Armor'))

    def do_sword(self, args):
        "Cost: 100 gold"
        if self.shop.checkout(self.player.gold, 'Sword', 'items'):
            self.add_inventory('items', self.shop.get_item('Sword'))

    def do_money(self, args):
        "Money"
        print('You have: ' + str(self.player.gold) + ' gold!')

    def do_exit(self, args):
        "Exit shop"
        return True

    def add_inventory(self, key, item):
        self.player.gold -= self.shop.shop_items[item[0]][0]
        self.player.inventory[key].append(item)
