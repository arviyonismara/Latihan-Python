#casting
#merubah tipe data

##Data Integer
print("==========INTEGER")
data_int = 9
print("data = ",data_int, "bertipe",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan bernilai 'False' jika bernilai 0
print("data = ",data_float, "bertipe",type(data_float))
print("data = ",data_str, "bertipe",type(data_str))
print("data = ",data_bool, "bertipe",type(data_bool))

## Data FLoat
print("\n==========FLOAT")
data_float = 9.5
print("data = ",data_float, "bertipe",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #akan bernilai 'False' jika bernilai 0
print("data = ",data_int, "bertipe",type(data_int))
print("data = ",data_str, "bertipe",type(data_str))
print("data = ",data_bool, "bertipe",type(data_bool))

## Data FLoat
print("\n==========BOOL")
data_bool = False
print("data = ",data_bool, "bertipe",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ",data_int, "bertipe",type(data_int))
print("data = ",data_str, "bertipe",type(data_str))
print("data = ",data_float, "bertipe",type(data_float))

## Data FLoat
print("\n==========STRING")
# data_str = 'Ucup' string tidak bisa dirubah ke int
data_str = '10' # untu itu string hanya bisa berisi angka agar bisa cast ke int
print("data = ",data_str, "bertipe",type(data_str))

data_int = int(data_str)
data_float = float(data_str) 
data_bool = bool(data_str)
print("data = ",data_int, "bertipe",type(data_int))
print("data = ",data_float, "bertipe",type(data_float))
print("data = ",data_bool, "bertipe",type(data_bool))