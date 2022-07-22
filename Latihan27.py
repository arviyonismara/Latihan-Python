#Looping List

# for loop
kumpulan_angka = [4,3,2,7,6,5,4,1]

for kumpulan in kumpulan_angka:
	print(f"angka = {kumpulan}")

nama_peserta = ["dadang","diding","dudung","dedeng"]
for peserta in nama_peserta:
	print(f"nama peserta = {peserta}")

# for loop dan range
kumpulan_angka = [10,5,4,2,7,2]
panjang = len(kumpulan_angka)
for i in range(panjang):
	print(f"angka = {kumpulan_angka[i]}")

# while
print("\nwhile loop")
kumpulan_angka = [10,5,4,2,7,2]
panjang = len(kumpulan_angka)
i = 0
while i<panjang:
	print(f"angka = {kumpulan_angka[i]}")
	i += 1

# list comprehension
print("\nlist Comprehesion")
data = ["dadang",1,2,3,"dedeng"]
[print(f"data={i}") for i in data]

kumpulan_angka = [10,5,4,2,7,2]
kuadrat = [i**2 for i in kumpulan_angka]
print(kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list):
	print(f"index = {index}, data = {data}")