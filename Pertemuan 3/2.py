pesan1 = { "id":"Masukkan nama Anda: ","en":"Please input your name: " }
pesan2 = { "id":"Selamat datang Bpk./Ibu.: ","en":"Welcome Mr./Mrs." }
kode = input("Language/Bahasa : (id ->Indonesia, en->English ): ")
nama = input(pesan1[kode])
text = pesan2[kode]
print(text + nama)