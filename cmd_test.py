import cmd
from shopv2 import Shop


class Shop_loop(cmd.Cmd):

    prompt = '->'

    def __init__(self, player, username):
        super().__init__()
        self.player = player
        self.usernamn = username
        self.shop = Shop(player)

    def do_small_potion(self, args):
        "Cost: 10 gold"
        if self.shop.checkout(
            self.player.gold, 'Small potion'
        ):
            self.add_inventory('potions', self.shop.small_potion)

    def do_luck_potion(self, args):
        "Cost: 30 gold"
        if self.shop.checkout(
            self.player.gold, 'Luck potion'
        ):
            self.add_inventory('potions', self.shop.luck_potion)

    def do_armor(self, args):
        "Cost: 40 gold"
        if self.shop.checkout(
            self.player.gold, 'Armor'
        ):
            self.add_inventory('items', self.shop.armor)

    def do_sword(self, args):
        "Cost: 40 gold"
        if self.shop.checkout(
            self.player.gold, 'Sword'
        ):
            self.add_inventory('items', self.shop.sword)

    def do_money(self, args):
        "Money"
        print('You have: ' + str(self.player.gold) + ' gold!')

    def add_inventory(self, key, item):
        self.player.gold -= self.shop.shop_items[item[0]]
        self.player.inventory[key].append(item)

    def do_exit(self, args):
        "Exit shop"
        return True


import entities
a = entities.Knight()
a.name = 'pelle'
a.initiativ = 1
a.agility = -11
a.endurance = 1
a.gold = 100


if __name__ == "__main__":
    Shop_loop(a, 'username').cmdloop()
