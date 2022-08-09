# latihan enkapsulasi
class Hero:

	def __init__(self, name, health, armour):
		self.name = name
		self.__health = health
		self.__armour = armour
		# self.__info = "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)
		# return self.__info

	@property
	def armour(self):
		pass

	@armour.getter
	def armour(self):
		return self.__armour

	@armour.setter
	def armour(self, input):
		self.__armour = input

	@armour.deleter
	def armour(self):
		print("armour didelete")
		self.__armour = None

sniper = Hero("Sniper", 100, 10)
# print(sniper.getHealth())
print(sniper.info)
sniper.name = "Dadang"
print(sniper.info)

print("getter dan setter untuk __armour")
print(sniper.armour)
sniper.armour = 50
print(sniper.armour)

print("delete armour")
del sniper.armour
print(sniper.__dict__)