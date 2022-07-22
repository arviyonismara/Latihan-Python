# program list buku

list_buku = []
while True:
	print("\nMasukan data Buku")
	judul = input("Judul\t:")
	penulis = input("penulis\t:")

	buku_baru = [judul, penulis]
	list_buku.append(buku_baru)

	print("\n\n","="*10,"Data Buku","="*10)
	for index,buku in enumerate(list_buku):
		print(f"{index+1} | {buku[0]} | {buku[1]}")
	
	print("\n\n","="*20)
	isLanjut = input("apakah dilanjutkan? Y/N")

	if isLanjut == "n":
		break
print("PROGRAM SELESAI")