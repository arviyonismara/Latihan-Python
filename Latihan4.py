#operasi Aritmatika

a = 10
b = 3

#operasi tambah +
hasil = a+b
print(a,"+",b,"=",hasil)

#operasi kurang -
hasil = a-b
print(a,"-",b,"=",hasil)

#operasi kali *
hasil = a*b
print(a,"*",b,"=",hasil)

#operasi bagi /
hasil = a/b
print(a,"/",b,"=",hasil)

#operasi eksponen (pangkat) **
hasil = a**b
print(a,"**",b,"=",hasil)

#operasi modulus %
hasil = a%b
print(a,"%",b,"=",hasil)

#operasi floor division(pembulatan kebawah) //
hasil = a//b
print(a,"//",b,"=",hasil)

#prioritas operasi, operational precedence
"""
1. ()
2. exponen **
3. perkalian dan teman2nya * / ** % // 
4. pertambahan dan pengurangan + -"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, "=",hasil)
#urutan prioritas () -> ** -> * -> +

#contoh
hasil = x + y * z
print(x,'+',y,'*',z,"= ",hasil)
#output = 11

hasil = (x + y) * z
print("(",x,'+',y,") *",z,"= ",hasil)
#output = 20
