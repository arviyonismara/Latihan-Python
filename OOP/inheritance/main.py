class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

class Hero_intelligent(Hero): # sub class yang meng inheritance dari Hero
	pass

class Hero_strength(Hero): # sub class yang meng inheritance dari Hero
	pass

Lina = Hero("Lina", 100)
techies = Hero_intelligent('techies', 50) # meng inheritance dari Hero
Nigg = Hero_strength("Nigg", 400)
print(Lina.name)
print(techies.name)
print(Nigg.name)