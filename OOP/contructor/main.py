class hero():
	def __init__(self, inputNama, inputPower, inputArmor, inputStrength, inputHealth): 
		# si __init__ akan selalu dieksekusi pertama kali ketika program di run
		self.name = inputNama
		self.power = inputPower
		self.armor = inputArmor
		self.strength = inputStrength
		self.health = inputHealth
# cara sebelumnya
# hero1.nama = "sniper"
# hero1.health = 300

hero1 = hero("Sniper", 85, 70, 90, 250)
hero2 = hero("Nigge", 60, 75, 85, 320)
hero3 = hero("Gintama", 90, 90, 90, 400)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
