class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    #method ini hanya berlaku untuk object / self
    def get_jumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def get_jumlah1():
        return Hero.__jumlah

    #method static (decorator) nempel ke object dan class
    @staticmethod
    def get_jumlah2():
        return Hero.__jumlah

    @classmethod
    def get_jumlah3(cls): #cls adalah argument untuk menampung class
        return cls.__jumlah

sniper = Hero('sniper')
print(Hero.get_jumlah2())
riki = Hero('riki')
print(sniper.get_jumlah2())
drowranger = Hero('drowranger')
print(Hero.get_jumlah3())