from leaderboard import Leaderboard


class End:
    def __init__(self, player, username):
        self.player = player
        self.username = username
        self.death_check()

    def death_check(self):
        if self.player.endurance <= 0:
            self.on_death()
        else:
            self.on_life()

    def on_death(self):
        print(
            'You have been slain in the dungeon\n'
            'Your score is being saved to the leaderboard.'
            )
        Leaderboard().add_score(
            f'{self.username} the {self.player.name}', self.player.gold)
        Leaderboard().get_scores()
        print(
            'Your hp, gold and items are going to be reset.\n'
            'Let\'s see if you can get a better score if you try again')
        self.reset_player()

    def on_life(self):
        print(
            f'Congratulations, {self.username}, you have survived the dungeon'
            '\n... This time.\n\nYou made it out with\n'
            f'{self.player.endurance} Hp left and {self.player.gold} gold\n'
            'You will be brought back to the entrance(the main menu)\n'
            'where you can spend some of your hard earned gold\n'
            'or just go for another run straight away.\n'
            'You could also quit the game, but let\'s not mention that')

        self.player.inventory['potions'] = []

    def reset_player(self):
        self.player.__init__()
