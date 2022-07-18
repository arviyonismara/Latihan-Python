# Date & Time

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)

# tanggal = dt.date(2005,10,10)
# print(tanggal)
print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lhr = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah {tanggal_lhr}")
print(f"Harinya adalah : {tanggal_lhr:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lhr
umur_tahun = umur_hari.days // 365
print(f"Harinya adalah : {tanggal_lhr:%A}")
print(f"umur anda adalah: {umur_tahun} tahun")