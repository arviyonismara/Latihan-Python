'''args'''

# memasukkan data/argument

def fungsi(nama,tinggi,berat):
	print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Ucup", 174, 55)

def fungsi(data_list):
	data = data_list.copy()
	nama = data[0]
	tinggi = data[1]
	berat = data[2]
	print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Otong",180,75])

def fungsi(*args): # tidak harus bernama args #menggunakan args agar tidak menggunakan list
	nama = args[0]
	tinggi = args[1]
	berat = args[2]
	print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
	
fungsi("Arvie", 173, 60)

#Studi kasus
def tambah(*data): # conth unutk mengambil banyak data sekaligus
	# data tipenya adalah tuple, dia bisa di iterasi
	output = 0
	for angka in data:
		output += angka
	return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")
