# Latihan Perulangan membuat segitiga bintang

sisi = 10

# 1. Menggunaka for
# dummy variable
# count = 1
# for i in range(sisi):
# 	print("*"*count)
# 	count += 1

# 2. Menggunakan While
# count = 1
# while True:
# 	print("*"*count)
# 	count += 1

# 	if count > sisi:
# 		break

# 3. Hanya Ganjil saja
print("awal while")
count = 1
while True:
	# akan printjika ganjil
	if count%2 :
		print("*"*count)
		count += 1
	else:
		# akan kembali keatas jika ganjil
		count += 1
		continue
	# akan break jika count melebihi sisi
	if count > sisi:
		break
print("akhir while\n")

# 4. hanya ganjil saja
print("awal while")
count = 1
spasi = int(sisi/2)

while True:
	if count%2:
		# print jika ganjil
		print(" "*spasi,"+"*count)
		spasi -= 1
		count += 1
	else:
		# akan kembali keatas jika ganjil
		count += 1
		continue
	# akan break jika count melebihi sisi
	if count > sisi:
		break
count = sisi - 1
spasi = 1
while True:
	if count%2:
		print(" "*spasi,"+"*count)
		spasi += 1
		count -= 1
	else:
		count -= 1
		continue
	if count < 0:
		break
