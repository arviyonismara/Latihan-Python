''' Fungsi dengan Argument (input) '''

'''
def nama_fungsi(argument):
	Badan fungsi
'''

def hello_world(nama):
	'''Fungsi hello world menerima input dengan variabel nama'''
	print(f"Selamat datang {nama}")

hello_world("Ryan")

def tambah(angka1,angka2):
	'''Fungsi Tambah'''
	hasil = angka1 + angka2
	print(f"hasil dari {angka1} + {angka2} = {hasil}")

tambah(1, 5)
tambah(100, 57)

def say_hi(list_peserta):
	'''Ini adalah fungsi say hi'''
	data_peserta = list_peserta.copy()
	for peserta in data_peserta:
		print(f"yang terhormat {peserta}")

anggota  = ["Ucup", "Otong", "kaesar", "Raihan"]
say_hi(anggota)