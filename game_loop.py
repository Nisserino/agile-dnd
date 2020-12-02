import cmd


class GameLoop(cmd.Cmd):
    intro = ''
    prompt = ''

    def do_move(self, arg):
        ''
        pass

    # extra func if PO wants it
    def do_look_around(self, arg):
        ''
        pass

    def do_hp(self, arg):
        'Check how much health points are left'
        pass
