from Hitung import tambah, kali, __str__

pesan = "ini kode program utama"
print(pesan)

x = float(input("Masukkan nilai-1 : "))
y = float(input("Masukkan nilai-2 : "))
print("Ini fungsi %s" %(__str__))

hasil = tambah(x, y)
print("Hasil penjumlahan %f dan %f adalah %f" %(x, y, hasil))

hasil = kali(x, y)
print("Hasil perkalian %f dan %f adalah %f" %(x, y, hasil))