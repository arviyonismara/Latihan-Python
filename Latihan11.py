# Operation String

data = 'ini adalah String'
print(data)
print(type(data))

# 1. Cara membuat String
'''
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
'''

data = 'Menggunakakn single quote'
print(data)
data = "menggunakan souble quote"
print(data)

print('"Hello World 1"')
print("'Hello World 2'")

# 2. Menggunakan tanda \
#membuat tanda ' menjadi String
print('mari shalat jum\'at')
print('you\'ll be fine')

#Backlash
print("C:\\user\\ucup")

#tab
print("ucup\t\t\totong, semaking jauhan")

#backspace
print("ucup \botong, jadi deketan")

#newline
print("baris pertama.\nbaris kedua.") #LF -> line feed ->unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return -> dipakai windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') #akan salah pathnya

# menggunakan Raw String
print(r'C:\new folder')

#multiline literal String
print("""
Nama  : Ucup
Kelas : 4
""")

#multiline literal String dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD \new normal
""")