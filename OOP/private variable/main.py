class Hero():

	# clas variable
	jumlah = 0

	def __init__(self,name,health):
		self.name = name
		self.health = health

		# private instance variable
		self.__private = "private"
		# private instance protected
		self._protected = "protected" # sebenarnya sama dengan public

Lani = Hero("Lani", 400)

print(Lani.__dict__)
Lani._protected = "testing"
print(Lani.__dict__)
print(Lani._protected)
print(Lani.__private) # akan muncul error karena private
print(Lani.__dict__)