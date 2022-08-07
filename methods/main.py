class Hero():
	# class variable
	jumlah_hero = 0

	def __init__(self, inputname, inputpower, inputhealth, inputarmour):
		# instance variable
		self.name = inputname
		self.power = inputpower
		self.health = inputhealth
		self.armour = inputarmour

	# void fungction, method tanpa return
	'''method menampilkan nama'''
	def siapa(self):
		print("namaku adalah "+ self.name)

	# method dengan argumen
	'''method menambah darah'''
	def healthUp(self, up):
		self.health += up

	# method dengan return
	'''method mencetak darah'''
	def getHealth(self):
		return self.health

hero1 = Hero("Balmond", 500, 750, 600)
hero2 = Hero("Jett", 600, 400, 500)

hero1.siapa()
hero1.healthUp(35)

print(hero1.getHealth())