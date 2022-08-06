class Mahasisiwa():
	def __init__(self, inputNama, inputNIM, inputProdi):
		self.nama = inputNama
		self.nim = inputNIM
		self.prodi = inputProdi

mhs1 = Mahasisiwa("Arvie Arvearie Y", "A11.2020.12792", "Teknik Informatika")
mhs2 = Mahasisiwa("Bima Rakajati", "A11.2020.13888", "Teknik Informatika")
mhs3 = Mahasisiwa("Safrizal Cahya N", "A11.2020.12798", "Teknik Informatika")

print(mhs1.__dict__)
print(mhs2.__dict__)
print(mhs3.__dict__)