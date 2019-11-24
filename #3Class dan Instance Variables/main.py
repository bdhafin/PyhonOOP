class Hero:
    #class variable
    jumlah = 0
    
    def __init__(self, name, health, attack, armor):
        #instance variable
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlah += 1 #mengakses class variable
        print("Membuat hero dengan nama :", self.name)


hero1 = Hero('sniper', 100, 10, 4)
hero2 = Hero('mirana', 100, 20, 2)

print('Jumlah hero sekarang :', Hero.jumlah)
