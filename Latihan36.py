'''Type hints untuk fungsi'''

# bentuk standat fungsi yang udah kita pelajari

def fungsi(parameter):
	print(parameter)

print("ucup")

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
	'''FUNGSI DENGAN HINTS'''
	output = 10**argument
	return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

