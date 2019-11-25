class Hero:

    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    #getter
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    #setter
    def diserang(self, enemyPower):
        self.__health -= enemyPower

    def set_attack(self, nilaiBaru):
        self.__attack = nilaiBaru

#Awal dari game
earthshaker = Hero('earthshaker', 50, 5)

#Game berjalan
print(earthshaker.get_name())
print(earthshaker.get_health())
earthshaker.diserang(5)
print(earthshaker.get_health())