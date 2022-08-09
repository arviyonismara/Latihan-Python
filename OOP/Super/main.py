class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("{} dengan Health: {}".format(self.name, self.health))

class Hero_intelligent(Hero): # sub class yang meng inheritance dari Hero
	def __init__(self, name):
		# self.name = name # bisa begini
		# self.health = 100
		# Hero.__init__(self, name, 100) # atau begini
		super().__init__(name,100) # super berarti mengambil method (def__init__)
		super().showInfo()

class Hero_strength(Hero): # sub class yang meng inheritance dari Hero
	def __init__(self, name):
		# self.name = name
		# self.health = 200
		# Hero.__init__(self, name, 100)
		super().__init__(name,200)
		super().showInfo()

Lina = Hero_intelligent("Lina")
Doom = Hero_intelligent("Doom")

