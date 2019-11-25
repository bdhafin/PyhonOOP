class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def show_info(self):
        print("{} health : {}".format(self.name, self.health))

class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    #override method
    def show_info(self):
        print("{}\n\ttipe: intelligent, \n\t health: {}".format(
            self.name,
            self.health
            )
        )

class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.show_info()
axe.show_info()