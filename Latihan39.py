# Lambda Function
# bisa membuat program kita lebih simple

def f_kuadrat(angka):
	return angka**2

print(f"hasil kuadrat = {f_kuadrat(3)}")

# kita coba dengan lambda contoh 1
# output = lambda argument: expression
kuadrat = lambda angka: angka**2
print(f"hasil kuadrat = {kuadrat(5)}")

# Contoh 2
pangkat  = lambda num,pow: num**pow
print(f"hasil lambda pangkat = {pangkat(5,3)}")

## kegunaan lambda apa?

# sorting untuk list
data_list = ["Otong", "Ucup", "Bapul"]
data_list.sort()
print(f"sorted list{data_list}")

# sorting dia pakai panjang (len)
data_list.sort(key=len)
print(f"sorted list by len = {data_list}")

# atau
def panjang_nama(nama):
	return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by len = {data_list}")

# sort pakai lambda 
data_list = ["Otong", "Ucup", "Bapul"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by len = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def kurang_dari_lima(angka):
	return angka < 5
data_angka_baru = list(filter(kurang_dari_lima,data_angka)) # cara biasa
data_angka_baru = list(filter(lambda x:x<7, data_angka)) # cara lambda
print(data_angka_baru)

# genap
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def genap(angka):
	if angka % 2 == 0:
		return angka
data_angka_genap = list(filter(genap,data_angka)) # cara biasa
print(data_angka_genap)
data_angka_genap = list(filter(lambda x:x%2==0, data_angka)) # cara lambda
print(data_angka_genap)

# ganjil
data_angka_ganjil = list(filter(lambda x:x%2!=0, data_angka)) # cara lambda
print(data_angka_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:x%3==0, data_angka))
print(data_3)

# Anonymous function
# currying <- Haskell Curry

def pangkat(angka,n):
	hasil = angka ** n
	return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi
def pangkat(n):
	return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(5)}")
print(f"pangkat bebas = {pangkat(4)(5)}") # dibaca 5**4