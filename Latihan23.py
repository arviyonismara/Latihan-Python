## Operasi & manipulasi data List

#index   0/-3    1/-2    2/-1
data = ["Bapul","ucup", "nibba"]

#mengambil data dati list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah {data_terakhir}")

data_ucup = data[-2]
print(f"data Ucup adalah {data_ucup}")

#mengambil info data dalam list
panjang_data = len(data)
print(f"panjang data adalah {panjang_data}")

## Manipulasi data List

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = {data}")
data.insert(1,"Asep")
print(f"data sesudah ditambah = {data}")

# menambah di akhir
data.append("Jambul")
print(f"data sesudah diAppend = {data}")

# Menambahkan list dengan list
data_baru = ["Ujang", "Usop", "Dadang"]
data.extend(data_baru)
print(f"data sesudah diExtend = \n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data yang telah dirubah = \n{data}")

#meremove data

data.remove("Ujang")
print(f"data yang telah dihanpus = \n{data}")

# data.remove("Ucup") ini akan error karena "Ucup" tidak ada dalam list

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = {data_akhir}")