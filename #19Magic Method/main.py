class Mangga:
    
    #magic method
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):
        return "Debug : Mangga: {} dengan jumlah: {}".format(self.name, self.jumlah)

    def __str__(self):
        return "Mangga: {} dengan jumlah: {}".format(self.name, self.jumlah)

    def __add__(self, object):
        return self.jumlah + object.jumlah

    #cara merubah .__dict__
    @property
    def __dict__(self):
        return "object ini mempunyai nama dan jumlah"

belanja1 = Mangga('arumanis', 10)
belanja2 = Mangga('cengkir', 5)
print(belanja1)
#print(repr(belanja1))
print(belanja2)

#penggunaan __add__
print(belanja2 + belanja1)
print(belanja1.__dict__)