class Hero:

	__jumlah = 0

	def __init__(self,name):
		self.__name = name
		Hero.__jumlah += 1

	def getJumlah(self):
		return Hero.__jumlah

sniper = Hero("Sniper")
print(Hero.__jumlah)
balmond = Hero("Balmond")
archer = Hero("Archer")