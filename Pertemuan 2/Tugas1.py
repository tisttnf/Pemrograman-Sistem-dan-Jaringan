"""
1. Tentukan tipe data dari nilai nilai variabel berikut ini (Anda dapat menggunakan fungsi type()
untuk kemudahan, contoh: x = 6 → type(x) ):
• nama = 'Hendra'
• gender = “L”
• umur = 25
• Berat = “60”
• jawab = True
• data = None
• xyz = 2.7
"""
nama = 'Hendra'
gender = "L"
umur = 25
Berat = "60"
jawab = True
data = None
xyz = 2.7

print(type(nama))
print(type(gender))
print(type(umur))
print(type(Berat))
print(type(jawab))
print(type(data))
print(type(xyz))

# 2. Tuliskan hasil dari kode program sederhana berikut ini :
nama = "Peter Parker"
Title = "Mr."
message1 = "Hello"
message2 = "Nice to meet you"
text = message1 + " , " + Title + nama + " , " + message2
print(text)

""" 3. Perhatikan kode program berikut ini, coba di jelaskan mengapa program tidak berjalan dengan
benar, dan memunculkan kesalahan (error) ? Jelaskan penyebab masalahnya, dan apakah
solusinya. !
"""
# X = 200
# Y = '50'
# Z = X + Y
# print("Penjumlahan " + X + " dan " + Y + " adalah : " + Z )
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Penyebabnya error karena menggabungkan integer dan string
# Solusinya menggunakan fungsi konversi parse int() dari str menjadi int dan parse str() dari int menjadi str
X = 200
Y = '50'
Z = X + int(Y)
print("Penjumlahan " + str(X) + " dan " + str(Y) + " adalah : " + str(Z))

"""
4. Perhatikan kode program berikut ini, lengkapilah tanda ........ dengan pernyatan atau instruksi
yang tepat sehingga kode program berikut ini akan menampilkan output : 
"Nama Depan Anda : TUTI Dan nama belakang Anda : marutikelopo"

Brikut kode program yang perlu Anda lengkapi :
nama = "Tuti Marutikelopo"
nama_depan = nama[:4]
...................................
Pesan1 = "Nama Depan Anda : "
........................................
text = Pesan1 + ........ + Pesan2 + nama_belakang.lower()
.......................................
"""
nama = "Tuti Marutikelopo"
nama_depan = nama[:4]
nama_belakang = nama[5:]
Pesan1 = "Nama Depan Anda : "
Pesan2 = "nama belakang Anda : "
text = Pesan1 + nama_depan.upper() + " Dan " + Pesan2 + nama_belakang.lower()
print(text)
