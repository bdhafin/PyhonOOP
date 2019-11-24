class Hero:
    
    #membuat __init__ method untuk inisiasi object
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

#memasukkan arguments pada inisiasi object
hero1 = Hero('sniper', 100, 10, 4)
hero2 = Hero('mirana', 100, 20, 2)

print('Nama\t:', hero1.name,
      '\nHealth\t:', hero1.health,
      '\nAttack\t:', hero1.attack,
      '\nArmor\t:', hero1.armor)

print("=" * 50)

print('Nama\t:', hero2.name,
      '\nHealth\t:', hero2.health,
      '\nAttack\t:', hero2.attack,
      '\nArmor\t:', hero2.armor)
