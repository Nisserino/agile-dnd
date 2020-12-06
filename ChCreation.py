class ChCreation:
    def __init__(self, username, choice, hero):
        self.username = username
        self.choice = choice
        self.hero = hero
    
    def user(self):
        self.username = input('Whats your username?')
        print(f'Welcome to Dungeons and Dragons {self.username}!')
        
        self.choice = input('Whats your choice')
        if self.choice == 'Rider':#1
            self.hero = Rider()
        elif self.choice == 'Wizard':#2
            self.hero == Wizard()
        elif self.choice == 'Thief':#3
            self.hero == Thief()

