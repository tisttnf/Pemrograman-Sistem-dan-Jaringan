import Hitung

pesan = "ini kode program utama"
print(pesan)

x = float(input("Masukkan nilai-1 : "))
y = float(input("Masukkan nilai-2 : "))
print("Ini fungsi %s" %(Hitung.__str__))

hasil = Hitung.tambah(x, y)
print("Hasil penjumlahan %f dan %f adalah %f" %(x, y, hasil))

hasil = Hitung.kali(x, y)
print("Hasil perkalian %f dan %f adalah %f" %(x, y, hasil))