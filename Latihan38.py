'''**Kwargs'''

def fungsi(nama,tinggi,berat):
	'''fungsi biasa'''
	print(f"{nama} punya tinggi {tinggi} punya berat {berat}")

fungsi("Arvie", 174, 55)

def fungsi (**kwargs): # akan merubah menjadi dictionary
	'''fungsi biasa'''
	nama = kwargs["nama"] # mengambil key untuk refrence
	tinggi = kwargs["tinggi"]
	berat = kwargs["berat"]
	print(f"{nama} punya tinggi {tinggi} punya berat {berat}")
	
fungsi(nama="Ucup", tinggi= 183, berat=76) # output akan menjadi dictionary
#maka dari itu dapat mengambil key nya

# # Studi kasus

# def math(*args, **kwargs):
# 	if kwargs["option"] == "tambah":
# 		print("Operasi Penjumlahan")
# 	elif kwargs["option"] == "kali":
# 		print("operasi perkalian")
# 	return hasil

# hasil = math(1,2,3,4,5,6,7,8,9,option="tambah")

def math(*args, **kwargs):
	output = 0
	if kwargs["option"] == "tambah":
		for angka in args:
			output += angka
	elif kwargs["option"] == "kali":
		output = 1
		for angka in args:
			output *= angka
	return output

output = math(1,2,3,4,5,option="tambah")
print(f"hasil penjumlahan = {output}")
output = math(1,2,3,4,5,option="kali")
print(f"hasil perkalian = {output}")