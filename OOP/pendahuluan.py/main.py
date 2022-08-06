class Hero: # template
	pass


hero1 = Hero() # Object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.nama = "sniper"
hero1.health = 100

hero2.nama = "dorg"
hero2.health = 200

hero3.nama = "bopo"
hero3.health = 1000

print(hero1)
print(hero1.__dict__) # print as dictionary
print(hero1.nama)