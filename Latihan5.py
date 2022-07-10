#operasi komparasi
#setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#lebih besar dari >
print("===== lebih besar dari (>)")
hasil = a > 3
print(a,'>',3,'=',hasil)

#kurag dari
print("===== kurang dari (>)")
hasil = a < 3
print(a,'<',3,'=',hasil)

#lebih dari sama dengan (>=)
print("===== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = a >= 4
print(a,'>=',4,'=',hasil)

#kurang dari sama dengan (>=)
print("===== kurang dari sama dengan (>=)")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = a <= 4
print(a,'<=',4,'=',hasil)

#sama dengan (=)
print("===== sama dengan (=)")
hasil = a == 4
print(a ,'==' ,4, "=",hasil)

#tidak sama dengan (!=)
print("===== tidak sama dengan (!=)")
hasil = a != 4
print(a ,'!=' ,4, "=",hasil)
hasil = b != 4
print(b ,'!=' ,4, "=",hasil)

#'is' sebagai komparasi object / variable
x = 5 #ini adalah assigntment membuat object
y = 6

print("===== object identity 'is' ")
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

print("===== object identity 'is not' ")
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is not y = ',hasil)