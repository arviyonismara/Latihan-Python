class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("showInfo di class Hero")
		print("{} Health: {}".format(self.name, self.health))

class Hero_intelligent(Hero): # sub class yang meng inheritance dari Hero
	def __init__(self, name): # method ini tidak akan meng override karena memiliki parameter yang berbeda dari milik _init__ class Hero
		super().__init__(name,100) # super berarti mengambil method (def__init__)

	def showInfo(self): # overriding method akan meng-override method yang sama dalam kasus ini mengoverride def showInfo milik class Hero
		print("showInfo di sub-class Hero_Intelligent")
		print("{} \n\tTipe : Intelligent, \n\tHealth: {}".format(self.name, self.health))

class Hero_strength(Hero): # sub class yang meng inheritance dari Hero
	def __init__(self, name):
		super().__init__(name,200)

Lina = Hero_intelligent("Lina")
Doom = Hero_strength("Doom")

# Lina.showInfo()
Doom.showInfo()