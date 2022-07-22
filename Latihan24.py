# Operasi list lanjut
data_angka = [1,5,4,6,2,6,8,6,4,8,7,9,7,3]
print(f"data angka = {data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Bapul","ucup", "nibba", "ujang"]
print(f"data = {data}")

index_dudung = data.index("nibba")
print(f"posisi \"nibba\" di index {index_dudung}")

# mengurutkan List
# angka
print(f"data angka sebeum di sort = {data_angka}")
data_angka.sort()
print(f"data angka sesudah di sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# Balik listnya / reverse
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")