# Nested List

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"List biasa = {data_list_biasa}")

list_2D = [data_0, data_1]
print(f"List 2D = {list_2D}")

list_2D = [data_0, data_1,5,6,7] #contoh lain
print(f"List 2D = {list_2D}")

peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 30, "Laki-laki"]
peserta_2 = ["Rahma", 32, "Perempuan"]

List_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {List_peserta}")

for peserta in List_peserta:
	print(f"nama\t: {peserta[0]}")
	print(f"umur\t: {peserta[1]}")
	print(f"gender\t: {peserta[2]}\n")

# dengan reference
list_copy = List_peserta.copy()
print(f"peserta = {list_copy}")
peserta_0[0] = "Michael"
print(f"peserta = {list_copy}")
print(f"peserta = {List_peserta}")