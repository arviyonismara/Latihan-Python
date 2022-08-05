# Standart Library
# Standart Library adalah library yang sudah tersedia dari python, pengguna tinggal import untuk menggunakan
from asyncore import read
import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")

print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","e","f"]
data_count = Counter(data)
print(f"data count: {data_count['a']}")
print(f"data count: {data_count['c']}")

import io
file = io.open("file_text.txt","r")
print(file.read())