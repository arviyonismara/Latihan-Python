class A:
	def method_A(self):
		print("ini adalah method A")

class B:
	def method_B(self):
		print("Ini adalah ethod B")

class C(A,B): # class C meng inherit dua class sekaligus yaitu A dan B
	pass

objek = C()

objek.method_A()
objek.method_B()