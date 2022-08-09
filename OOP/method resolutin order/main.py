# method resolutin order // multiple inheritance

class A:
	def show(self):
		print("ini adalah show A")

class B:
	def show(self):
		print("Ini adalah show B")

class C(A,B): # urutannya adalah C A B
	pass
# class C(B,A): # urutannya adalah C A B
# 	pass

objek = C()
objek.show()
