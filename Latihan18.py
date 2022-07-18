# Looping for loop
# for kondisi:
#	  aksi

# for i in range(5): #artinya untuk semua i yang ada dalam range 5
# 	print("hello world",i)

angka1_list = [0,1,2,3,4]
print(angka1_list)

for i in angka1_list:
	print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
	print(f"i sekarang -> {i}")
print("akhir dari program 2 \n")

angka2_range = range(1,10) #range tersebut berarti akan dimulai dari 1 hingga 9

for i in angka2_range:
	print(f"i sekarang -> {i}")
print("akhir dari program 3 \n")

# menggunakan String

data_str = "saya ganteng abiezzz"
for huruf in data_str:
	print(huruf)
print("akhir dari program 3 \n")