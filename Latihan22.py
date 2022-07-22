# Latihan LIST

# kumpulan data numbers
data_angka = [1,5,3,2]
print(data_angka)

# kumpulan data String
data_string = ["ucup", "bapul", "Fikri"]
print(data_string)

# Kumpulan data boolean
data_bool = [True, False, True, False]
print(data_bool)

# kumpulan data campuran
data_campur = [1, "bapul", True, "Ucup"]
print(data_campur)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i for i in range(0,10)]
print(list_for)

list_for = [i**2 for i in range(0,10)] #contoh list kuadrat
print(list_for) 

# membuat list pake for dan if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)