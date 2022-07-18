# Operator dalam bentuk methods
## menambah case dari String

# merubah semua ke Uppercase Upper()
salam = "bro!"
print("normal = "+salam)
salam = salam.upper()
print("Upper = "+salam)

# merubah semua ke Lowercase 
saru = "InI HuRuF KoTOr"
print("normal = "+saru)
saru = saru.lower()
print("lower = "+saru)

## Pengecekkan dengan isX method
salam = "sist"
# contoh pengecekan lowercase
apakah_lower = salam.islower()
print(salam+" is lower = "+str(apakah_lower))
# contoh pengecekan Uppercase
apakah_upper = salam.isupper()
print(salam+" is upper = "+str(apakah_upper))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool

print(judul +" is title  = "+str(cek_judul))

## ngecek komponen startswith() endswith() <--- keren
cek_start = "MasBapul Ganteng".startswith("MasBapul")
print("start = "+str(cek_start)) #outbut bool

cek_end = "MasBapul Ganteng".endswith("Ganteng")
print("end = "+ str(cek_end))

## pengganbungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' tol '.join(pisah)
print(gabungan)

gabungan = "akutolsayangtolkamu"
print(gabungan.split('tol'))

#alokasi karakter rjust(), ljust(), center()
print(5*"="+"data"+"="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,':')
print("'"+tengah+"'")

#kebalikannya -> strip()
kanan = kanan.strip(":") #menghilangkan tanda :
print("'"+tengah+"'")
