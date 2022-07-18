# latihan Kalkulator sederhana

print(20*"=")
print("Kalkulator sederhana")
print(20*"="+"\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("Operator (+,-,X,/) : ")
angka_2 = float(input("masukan angka 2 = "))

if operator == "+":
	hasil = angka_1 + angka_2
	print(f"hasilnya adalah : {hasil}")
elif operator == "-":
	hasil = angka_1 - angka_2
	print(f"hasilnya adalah : {hasil}")
elif operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print(f"hasilnya adalah : {hasil}")
elif operator == "/":
	hasil = angka_1 / angka_2
	print(f"hasilnya adalah : {hasil}")
else:
	print("salah deck")
	