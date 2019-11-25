class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__healthStandard = health
        self.__attackStandard = attack
        self.__armorStandard = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMaximum = self.__healthStandard * self.__level
        self.__attack = self.__attackStandard * self.__level
        self.__armor = self.__armorStandard * self.__level

        self.__health = self.__healthMaximum

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} :\n\thealth = {}/{}\n\tattack = {}\n\tarmor = {}".format(self.__name, self.__level, self.__health, self.__healthMaximum, self.__attack, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMaximum = self.__healthStandard * self.__level
            self.__attack = self.__attackStandard * self.__level
            self.__armor = self.__armorStandard * self.__level

    def serang(self, enemy):
        self.gainExp = 50


slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.serang(axe)
slardar.serang(axe)
slardar.serang(axe)
print(slardar.info)
