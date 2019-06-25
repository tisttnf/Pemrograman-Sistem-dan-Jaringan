pesan1 = {"id":"Masukan nama: ",
          "en":"please input your name: "}
pesan2 = {"id":"Selamat satang: ",
          "en":"Welcome!"}

kode = input("Language/bahasa (id -> Indonesia, en -> English): ")

nama = input(pesan1[kode])
text = "%s %s" %(pesan2[kode],nama)

print(text)

# if kode.lower() == 'id':
#     nama = input(pesan1["id"])
#     text = f'{pesan2["id"]} {nama}'
#     print(text)
# elif kode.lower() == 'en':
#     nama = input(pesan1["en"])
#     text = f'{pesan2["en"]} {nama}'
#     print(text)oo