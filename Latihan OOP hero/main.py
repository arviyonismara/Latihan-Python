class Hero():
	
	def __init__(self, inputName, inputHealth, inputPower, inputArmour):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armour = inputArmour

	def serang(self, Lawan):
		print(self.name + " menyerang " + Lawan.name)
		Lawan.diserang(self, self.power) # memanggil method diserangagar otomatis muncul notif musuh diserang
	
	def diserang(self, Lawan, powerLawan):
		print(self.name + " diserang "+ Lawan.name)
		attack_received = powerLawan/ self.armour
		print("Serangan terasa : " + str(attack_received))
		self.health -= attack_received
		print("darah " + self.name + " tersisa " + str(self.health))


Balmond = Hero("Balmond", 1000, 50, 15)
Layla = Hero("Layla", 600, 85, 5)

Balmond.serang(Layla)
print("\n")
Layla.serang(Balmond)


