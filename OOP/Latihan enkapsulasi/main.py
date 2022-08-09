class Hero:

	__jumlah = 0

	def __init__(self, name, health, armour, power):
		self.__name = name
		self.__healthStandar = health
		self.__armourStandar = armour
		self.__powerStandar = power
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthStandar * self.__level
		self.__power = self.__powerStandar * self.__level
		self.__armour = self.__armourStandar * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "name {} : \n\thealth : {}/{} \n\tattack : {} \n\tarmour : {}".format(self.__name, self.__health,self.__healthMax, self.__power, self.__armour)

	@property
	def gainExp(self):
		pass

	@gainExp.getter
	def gainExp(self,addExp):
		self.exp += addExp
		if(self.__exp >= 100):
			print(self.__name, "level up")
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthStandar * self.__level
			self.__power = self.__powerStandar * self.__level
			self.__armour = self.__armourStandar * self.__level


Balmond = Hero("Balmond", 400, 20, 10)
print(Balmond.info)

Balmond.gainExp = 50
print(standar.info)