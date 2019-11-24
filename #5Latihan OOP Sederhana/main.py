class Hero:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
    
    def serang(self, enemy):
        print(self.name, 'menyerang', enemy.name)
        enemy.diserang(self, self.attack)

    def diserang(self, enemy, enemy_attack):
        print(self.name, 'diserang', enemy.name)
        damage = enemy_attack / self.armor
        print("serangan terasa :", damage)
        self.health -= damage
        print('darah ', self.name, 'tersisa', self.health)

sniper = Hero('sniper', 100, 10, 5)
riki = Hero('riki', 100, 20, 10)

sniper.serang(riki)
print('\n')
riki.serang(sniper)