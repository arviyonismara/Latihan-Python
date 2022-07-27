'''Latihan Fungsi'''
# program menghitung luas dan keliling persegi panjang
import os

# membuat header program

# # Header
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# #mengambil input user
# panjang = int(input("Masukan Panjang\t:"))
# lebar = int(input("Masukan Lebar\t:"))

# #program menghitung luas
# LUAS = panjang * lebar
# KELILING = 2*(panjang + lebar)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas \t= {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
	'''fungsi header'''
	os.system("cls")
	print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
	print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
	print(f"{'-'*40:^40}")

def input_user():
	'''Fungsi Input User'''
	#mengambil input user
	panjang = int(input("Masukan Panjang\t:"))
	lebar = int(input("Masukan Lebar\t:"))

	return panjang,lebar

def hitung_luas(panjang, lebar):
	#program menghitung luas
	return panjang*lebar

def hitung_keliling(panjang, lebar):
	#program mengitung keliling
	return 2*(panjang + lebar)

def display(message, value):
	print(f"Hasil perhitungan {message} = {value}")

while True:
	header()

	PANJANG, LEBAR = input_user()
	LUAS = hitung_luas(PANJANG, LEBAR)
	KELILING = hitung_keliling(PANJANG, LEBAR)

	display("Luas", LUAS)
	display("Keliling", KELILING)

	isContinue = input("apakah lanjut (y/n)?")
	if isContinue == "n":
		break

print("Program telah selesai terima kasih XD")
