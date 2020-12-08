import entities as e
import saveLoad as s


class CharacterCreation:
    def __init__(self, username, choice):
        self.username = ''
        self.hero = None
        self.choice = choice

    def user(self):
        if self.choice == 'Knight':
            self.hero = e.Knight()
        elif self.choice == 'Wizard':
            self.hero = e.Wizard()
        elif self.choice == 'Thief':
            self.hero = e.Thief()

        s.FileHandler.save(self.username, self.hero)
