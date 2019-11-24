class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self, name, health, attack, armor):
        #instance variable
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlah_hero += 1

    #membuat method tanpa argument atau return value
    def siapa(self):
        print("Namaku adalah", self.name)

    #method dengan argument
    def healthUp(self, up):
        self.health += up

    #method dengan return value
    def getHealth(self):
        return self.health    

    
hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('sven', 90, 5, 10)

#mengakses method
hero1.siapa()

#mengakses method dengan arguments
hero1.healthUp(10)
print(hero1.health)

print(hero1.getHealth())