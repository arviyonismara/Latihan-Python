class Hero:

	# private class variable
	__jumlah = 0

	def __init__(self,name):
		self.__name = name
		Hero.__jumlah += 1

	def getJumlah(self): # method ini berarti hanya berlaku untuk objek
		return Hero.__jumlah

	def getJumlah(): # method ini berarti tidak berlaku untuk objek / tapi berlaku untuk class (Hero)
		return Hero.__jumlah

	# method static # method ini bisa berlku untuk objek dan class
	@staticmethod # (decorator)
	def getJumlah2(): 
		return Hero.__jumlah

	@classmethod # (decorator)
	def getJumlah3(cls): # cls sebagai nama objek pengganti class
		return cls.__jumlah

sniper = Hero("Sniper")
print(Hero.getJumlah2())
# print(sniper.getJumlah())
# # print(Hero.getJumlah())
balmond = Hero("Balmond")
print(sniper.getJumlah2())
archer = Hero("Archer")
print(Hero.getJumlah3())
print(sniper.getJumlah3()) # bisa juga begini sama seperti yang diatas