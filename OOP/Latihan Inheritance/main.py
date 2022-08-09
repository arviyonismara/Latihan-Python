class Hero:

	def __init__(self,name):
		self.health_pool = [0,100,200,300,400,500]
		self.attack_pool = [0,10,20,30,40,50]
		self.armor_pool = [0,1,2,3,4,5]
		self.__name = name
		self.__exp = 0
		self.__level = 1

		def showInfo(self):
			print("{} \n\tlevel: {} \n\thealth: \n\tatack power: {} \n\tarmor: {}".format(
				self.__name,
				self.__level,
				self.__health,
				self.__attack,
				self.__armor
			))

		@property
		def health_pool(self):
			pass

		@property
		def attack_pool(self):
			pass
		
		@property
		def armor_pool(self):
			pass

		@property
		def LevelUp(self):
			pass

		@property
		def gainExp(self):
			pass

		@health_pool.setter
		def health_pool(self, input):
			self.__health_pool = input
		
		@attack_pool.setter
		def attack_pool(self, input):
			self.__attack_pool = input

		@armor_pool.setter
		def armor_pool(self, input):
			self.__armor_pool = input

		@gainExp.setter
		def gainExp(self, input):
			self.__exp += input
			if(self.__exp >= 100):
				self.LevelUp = self.__exp//100
				self.__exp %= 100

		@LevelUp.setter
		def LevelUp(self,input):
			self.__level += input
			self.__health = self.__health_pool[self.__level]
			
class Hero_Intelligent(Hero):
	
	def __init__(self, name):
		super().__init__(name)
		self.health_pool = [1,50,100,150,200,250]
		self.attack_pool = [0,20,40,60,80,100]
		self.attack_pool = [0,0.5,1,1.5,2,2.5]
		self.levelUp = 1

class Hero_Trength(Hero):

	def __init__(self, name):
		super().__init__(name)
		self.health_pool = [1,200,300,4000,500,6000]
		self.attack_pool = [0,20,40,60,80,100]
		self.levelUp = 1

Lina = Hero_Intelligent("Lina")
Balmond = Hero_Trength("Balmond")

Lina.showInfo()