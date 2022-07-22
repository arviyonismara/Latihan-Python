## Teknik meduplikat List

a = ["Bapul","ucup", "nibba", "ujang"]
print(f"a = {a}")
b = a

b = a # pass by references
print(f"b = {b}")

# kita akan merubah member dari a
# dengan ini akan merubah kedua list a dan b
a[1] = "Michael"
b.sort
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "Dadang" # dengan ini hanya list c yang berubah

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
