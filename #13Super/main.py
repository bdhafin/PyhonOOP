class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print("{} dengan health: {}".format(self.name, self.health))

class Hero_intelligent(Hero):

    def __init__(self, name):
        #Hero.__init__(self, name, 100) -> cara 1
        super().__init__(name, 100)
        super().show_info()
class Hero_strength(Hero):

    def __init__(self, name):
        #Hero.__init__(self, name, 200) -> cara 1
        super().__init__(name, 200)
        super().show_info()

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')
