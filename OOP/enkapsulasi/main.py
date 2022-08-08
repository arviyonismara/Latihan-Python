class Hero:

	def __init__(self, name, health, power):
		self.__name = name # menambahkan __ didepan agar variabel menjadi private
		self.__health = health
		self.__power = power

	# getter
	def getName(self):
		return self.__name
	def getHealth(self):
		return self.__health
	
	# setter
	def diserang(self, damage):
		self.__health -= damage

	def setDamage(self, newDamage):
		self.__power = newDamage

# awal dari game
mirana = Hero("Mirana", 500, 30)

print(mirana.__dict__)

# game berjalan

print(mirana.getName())
print(mirana.getHealth())
mirana.diserang(10)
print(mirana.getHealth())