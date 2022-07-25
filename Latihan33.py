'''Fungsi dengan kembalian (return)'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
# 		badang fungsi
# 		return output

# fungsi kuadrat
def kuadrat(x):
	'''fungsi kuadrat'''
	output = x**2
	return output

y = kuadrat(3)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(5)
print(z)

# fungsi tambah
def fungsi_tambah(angka1, angka2):
	'''fungsi return dengan multi input'''
	return angka1 + angka2

a = fungsi_tambah(10,7)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka1,angka2):
	tambah = angka1 + angka2
	kurang = angka1 - angka2
	kali = angka1 * angka2
	bagi = angka1 / angka2
	return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(25, 5)
print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")