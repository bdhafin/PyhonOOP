from hero import Hero_intelligent, Hero_strength

lina = Hero_intelligent('lina')
slardar = Hero_strength('slardar')

lina.show_info()
slardar.show_info()

lina.gain_exp = 200
slardar.gain_exp = 250

lina.show_info()
slardar.show_info()