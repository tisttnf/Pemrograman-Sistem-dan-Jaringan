from datetime import datetime 

sekarang = datetime.now()
tahun_sekarang = sekarang.year

tahun = int(input("Tahun Kelahiran Anda: "))
usia = tahun_sekarang - tahun

if usia <= 12 :
    golongan = "Anak-anak"
elif usia >= 13 and usia <= 24 :
    golongan = "Remaja"
elif usia >= 25 and usia <= 45:
    golongan = "Pemuda"
elif usia >= 46 and usia <= 150 :
    golongan = "Orang Tua"
else :
    golongan = "Gak mungkin"

print("Usia Anda saat ini %d Thn" %(usia))
print("Anda termasuk golongan %s" %(golongan))