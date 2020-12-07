class ChCreation:
    def __init__(self, username, hero):
        self.username = ''
        self.hero = hero
    
    def user(self):
        if Entity.heroType == 'Knight':#1
            self.hero = Knight()
        elif Entity.heroType == 'Wizard':#2
            self.hero == Wizard()
        elif Entity.heroType == 'Thief':#3
            self.hero == Thief()

        return FileHandler.save(self.username, self.hero)

