class Team:
	def setTeam(self, team):
		self.team = team
	def showTeam(self):
		print(self.team)

class Tipe_hero:
	def setTipe(self,tipe):
		self.tipe = tipe

	def showTipe(self):
		print(self.tipe)

class Hero(Team,Tipe_hero): # class Hero menginherit class team dan Tipe_hero
	def __init__(self,name,health):
		self.name = name
		self.health = health
	
Nibb = Hero("Nibb", 100) # disini dia class Hero
Nibb.setTeam("Merah") # disini dia class Team
Nibb.setTipe("Kiper") # disini dia class Tipe_Hero

Nibb.showTeam()
Nibb.showTipe()