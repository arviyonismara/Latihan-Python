# Latihan membuat package

import sains.matematika # sains = package , matematika = module & tambah dll = definisi
from sains import fisika # cara lain
from sains.fisika import gaya as force # cara lain

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")