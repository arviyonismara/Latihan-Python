# Dictionary
# dictionary (dict) -> associative array
# diakses menggunakan identifier -> key
data_list = ["nigger",1,2,"Bayi"]

data_dict = {
	'key1': 'value1',
	'key2':'value2'
}
print(data_dict)

data_dict = {
	'key': 'value',
	'cp':'Ucup',
	'tg':'Otong',
	'dg':'dudung',
	'numb':100,
	'list':data_list,
}
print(data_dict['tg'])
print(data_dict['numb'])
print(data_dict['cp'])
print(data_dict['list'],"\n")

# Operasi Dictionary
data_dict = {
	'cup' : 'Ucup surucup',
	'pul': 'Bapul Barapul',
	'hma': 'Cantik Sekali'
}

#pangjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary = {LENDICT}")

#mengecek key exist atau tidak
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

#mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict['cup'] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep sikasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"pali":"pali palpalipali"}) # kalo tidak ada bakal menambah dictionary
print(data_dict)

#mendelete dictionary
del data_dict["sep"]
print(data_dict)

# Dictionary Loop

teman_teman ={
	'cup':'ucup surucup',
	'tong': 'otong sorotong',
	'pul':'Bapul Surupul',
	'bol':'bobol sorobol'
}

# looping firts try (yang keluar adalah keynya)

for teman in teman_teman:
	print(teman)

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
	print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
	print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
	print(item)

for key,value in teman_teman.items():
	print(f"key = {key}, value = {value}")