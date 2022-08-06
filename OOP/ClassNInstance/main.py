class Hero():
	# class variable
	jumlah = 0 # variable static variable yang menemperl apda class

	def __init__(self, inputNama, inputPower, inputArmor, inputStrength, inputHealth): 
		# Instance variable (variable yang menempel pada objek(pada kasus ini hero1,2,3))
		self.name = inputNama
		self.power = inputPower
		self.armor = inputArmor
		self.strength = inputStrength
		self.health = inputHealth
		Hero.jumlah += 1
		print("Membuat Hero dengan nama " + inputNama)

hero1 = Hero("Sniper", 85, 70, 90, 250)
print(Hero.jumlah)
hero2 = Hero("Nigge", 60, 75, 85, 320)
print(Hero.jumlah)
hero3 = Hero("Gintama", 90, 90, 90, 400)
print(Hero.jumlah)
