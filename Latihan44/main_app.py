# import sains

# hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = sains.fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = sains.matematika.scientific.kali(1,2,3,4,5)
# print(f"hasil kali = {hasil_kali}")

# from sains import * 

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(1,2,3,4,5)
# print(f"hasil kali = {hasil_kali}")

import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat3 = scientific.pangkat(3)
print(f"hasil pangkat = {pangkat3(5)}")