# format String

# contoh generic
nama = "marelene"
format_str = f"hello {nama}"

print(format_str)

# boolean
bool = False
format_str = f"boolean = {bool}"
print(format_str)

#angka
angka = 2002.2
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan jutaan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" #menjadi 2 angka dibelakang koma
print(format_str)

# menampikan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# memformat persent
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)
