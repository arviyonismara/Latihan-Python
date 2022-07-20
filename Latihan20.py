# Continue,  pass, break

# pass -> berfungsi sebagai dummmy, tidak akan dieksekusi
angka  = 0
while angka < 5:
	angka += 1
	if angka == 3:
		pass #ini tidak akan dieksekusi
	print(angka)

# Continue
angka = 0
print(f"angka sekarang = {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") #ini aksi satu
	if angka == 3:
		print("nice!")
		continue #akan membuat loop akan loncat ke step selanjutnya
		#dalam kasus ini ketika bernilai tiga, kata wassup tidak akan muncul
	print("wassup") # ini aksi dua
print("finish")

# Break
int = int(input("masukan batas: "))
angka = 0
while True:
	angka += 1
	print(f"angka sekarang -> {angka}")

	if angka == int:
		print("nice!!!!")
		break
	print("Whassup")
print("cukup")
	