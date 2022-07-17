# operasi logika atau boolean

#not, or, and, xor
print('====NOT====')
a = True
c = not a
print('data a = ',a)
print('-------- NOT')
print('data c = ',c) #outupt menjadi kebalikannya

print('\n====OR====') #hanya bernilai false jika keduanya False
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)

print('\n====AND====') #hanya bernilai True jika keduanya True
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,' =',c)
a = True
b = False
c = a and b
print(a,'and',b,' =',c)
a = True
b = True
c = a and b
print(a,'and',b,'  =',c)

print('\n====And====') #Akan bernilai True jika salah satunya True
a = False
b = False
c = a ^ b
print(a,'And',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'And',b,' =',c)
a = True
b = False
c = a ^ b
print(a,'And',b,' =',c)
a = True
b = True
c = a ^ b
print(a,'And',b,'  =',c)