class Hero:

	__jumlah = 0

	def __init__(self, name, health, armour, power):
		self.__name = name
		self.__healthStandar = health
		self.__armourStandar = armour
		self.__powerStandar = power
		self.__level = 1
		self.exp = 0

		self.__healthMax = self.__healthStandar * self.__level
		self.__power = self.__powerStandar * self.__level
		self.__armour = self.__armourStandar * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "name {} : \n\thealth : {}/{}".format(self.__name, self.__health,self.__healthMax)

Balmond = Hero("Balmond", 400, 20, 10)
print(Balmond.info)