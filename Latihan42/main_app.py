# module matematika dengan import

# import matematika # bisa juga from matematika import tambah,kali,pangkat / from matematika import *

# hasil_tambah = matematika.tambah(1,2,3,4)
# print(f"hasil tambah = {hasil_tambah}")
# hasil_kali = matematika.kali(2,4,6)
# print(f"hasil kali = {hasil_kali}")

# pangkat3 = matematika.pangkat(3)
# print(f"hasil pangkat3 = {pangkat3(4)}")

from matematika import tambah,kali,pangkat

hasil_tambah = tambah(1,2,3,4)
print(f"hasil tambah = {hasil_tambah}")
hasil_kali = kali(2,4,6)
print(f"hasil kali = {hasil_kali}")

pangkat3 = pangkat(3)
print(f"hasil pangkat3 = {pangkat3(4)}")

# bisa juga import matematika as math
# from matematika import tambah as add
# from matematika import kali as k
# dll