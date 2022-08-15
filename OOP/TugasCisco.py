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
		return "{} level {} : \n\thealth : {}/{} \n\tattack : {} \n\tarmour : {}".format(self.__name,self.__level, self.__health,self.__healthMax, self.__power, self.__armour)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if(self.__exp >= 100):
			print(self.__name, "level up")
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthStandar * self.__level
			self.__power = self.__powerStandar * self.__level
			self.__armour = self.__armourStandar * self.__level

	def serang(self, Lawan):
		print(self.__name + " menyerang " + Lawan.__name)
		self.gainExp = 50
		Lawan.diserang(self, self.__power)
	
	def diserang(self, Lawan, powerLawan):
		print(self.__name + " diserang "+ Lawan.__name)
		attack_received = powerLawan/ self.__armourStandar
		print("Serangan terasa : " + str(attack_received))
		self.__health -= attack_received
		print("darah " + self.__name + " tersisa " + str(self.__health)+ "\n")
		if self.__health < 0:
			print(self.__name + "sudah meniggal")


Balmond = Hero("Balmond", 400, 20, 40)
Jett = Hero("Jett", 300, 10, 60)

print(5*"=","Welcome to Raceto Game",5*"=")

while True:
	print("Option	:")
	print("1. Show Character")
	print("2. Choose character")
	print("3. quit game\n")
	option = int(input("Enter option : "))
	if option == 1:
		print(Balmond.info)
		print(Jett.info)
	elif option == 2:
		print("Hero list")
		print("1. Balmond")
		print("2. Jett")
		hero = int(input("Choose your Hero : "))
		if hero == 1:
			print("your hero = Balmond\n")
			print(Balmond.info)
			while True:
				play = input("do you want to attack jett? Y/N\n")
				if play == "y":
					Balmond.serang(Jett)
				elif play == "n":
					break
		elif hero == 2:
			print("your hero = Jett\n")
			print(Jett.info)
			while True:
				play = input("do you want to attack Balmond? Y/N")
				if play == "y":
					Jett.serang(Balmond)
				elif play == "n":
					break
	elif option == 3:
		break
print("End Game. Thanks for playing !!!")