import entities as e
import saveLoad as s


class CharacterCreation:
    def __init__(self, username, choice):
        self.username = username
        self.hero = None
        self.choice = choice
        self.create_instance()
        self.send_to_save((self.username, self.hero))

    def create_instance(self):
        if self.choice == 'Knight':
            self.hero = e.Knight()
        elif self.choice == 'Wizard':
            self.hero = e.Wizard()
        elif self.choice == 'Thief':
            self.hero = e.Thief()

    def send_to_save(self, data):
        s.FileHandler().save(data)
