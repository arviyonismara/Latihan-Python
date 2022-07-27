'''Default Argumen'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya)

#contoh 1
def say_hello(nama = 'Kamu'):
	'''Fungsi dengan default argument'''
	print(f"Hallo {nama}")

say_hello("Arvie")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa Kabar?"):
	'''Fungsi dengan satu input biasa dan satu default argumen'''
	print(f"Hai {nama}, {pesan}")

sapa_dia("Bapul", "Kamu ganteng")
sapa_dia("Ucup")

# Contoh 3
def hitung_pangkat(angka, pangkat = 2):
	hasil = angka**pangkat
	return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat = 2, angka = 5)
print(hasil)

#Contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
	hasil = input1 + input2 + input3 + input4
	return hasil

print(fungsi())
print(fungsi(input3 = 10))