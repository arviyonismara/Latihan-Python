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
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<7, data_angka))
print(data_angka_baru)