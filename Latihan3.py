#tipe data

#data integer
data_integer = 11
print("data: ",type(data_integer))
print("-bertipe : ",data_integer,"bertipe ",type(data_integer))

#data float
data_float = 1.5
print("data: ",type(data_float))
print("-bertipe : ",data_float,"bertipe ",type(data_float))

#data String
data_string = "Ucup"
print("data: ",type(data_string))
print("-bertipe : ",data_string,"bertipe ",type(data_string))

#data Boolean /bool
data_bool = False
print("data: ",type(data_bool))
print("-bertipe : ",data_bool,"bertipe ",type(data_bool))

##tipe data khusus
#bilangan kompleks
data_complex = complex(5,6)
print("data: ",type(data_complex))
print("-bertipe : ",data_complex,"bertipe ",type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data: ",type(data_c_double))
print("-bertipe : ",data_c_double,"bertipe ",type(data_c_double))