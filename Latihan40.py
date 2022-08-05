## Global and Local scope

nama_global = "Otong" # <- ini merupakan variable global

def fungsi():
	print(f"fungsi menampilkan {nama_global}")

fungsi()

for i in range(0,5):
	print(f"loop {i} - {nama_global}")

# percabangan 
if True:
	print(f"if menampilkan {nama_global}")

## Variable Locl Scope
def fungsi2():
	nama_local = "Ucup" # variable lokal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## Contoh 1: Penggunaan
# nama ="Ucup" bisa disini
def say_otong():
	print(f"Hello {nama}")
	
nama = "Otong"
say_otong()

## Contoh 2: merubah variable global
angka = 0
nama = "Ucup"

def ubah_angka(nilai_baru,nama_baru):
	global angka # fungsi ini mendapat akses merubah angka
	global nama
	angka = nilai_baru
	nama = nama_baru

print(f"angka sebelum dirubah = {angka}")
print(f"nama sebelum dirubah = {nama}")
ubah_angka(10,"Bapul")
print(f"angka setelah dirubah = {angka}")
print(f"nama setelah dirubah = {nama}")


## Contoh 3:
angka = 0
for i in range(0,5):
	angka += i
	angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
	angka = 10
	angka_dummy = 10

print(angka)
print(angka_dummy)