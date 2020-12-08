import cmd


class CombatLoop(cmd.Cmd):
    prompt = '-> '

    def __init__(self, dm, username):
        super().__init__()
        self.dm = dm
        self.username = username
        self.attack_order = []
        self.next_loop = 'move'

    def do_quit(self, arg):
        return True

#   - - - Unseen funcs - - -
    def deal_damage(self, attacker, blocker):
        pass

    def init_rolls(self):
        pass

#   - - - Cmd specific funcs - - -
    def preloop(self):
        self.dm.entity_spawner(self.dm.player.position)

    def postloop(self):
        Bouncer(self.dm, self.username, self.next_loop)
