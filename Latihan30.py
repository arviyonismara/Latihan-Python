# Copy Dictionary

teman_teman ={
	'cup':'ucup surucup',
	'tong': 'otong sorotong',
	'pul':'Bapul Surupul',
	'bol':'bobol sorobol'
}

friends = teman_teman.copy()

print(f"teman_teman : {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman['cup'] = 'Ucup sikeren'
print(f"teman_teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataBapul = friends.pop("pul")
print(f"data Bapul : {dataBapul}\n")
print(f"friends: {friends}\n")

# pop item dictionary (yang terakkhir ajah)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}")
print(f"friends: {friends}\n")