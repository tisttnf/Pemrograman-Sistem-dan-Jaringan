total = 0
rerata = 0

mulai = int( input("Masukkan nilai awal: ") )
batas = int( input("Masukkan nilai batas: ") )

for x in range(mulai,batas):
    total = total + x    

rerata = total / len(range(mulai,batas))

pesan1 = "Total nilai penjumlahan %d s.d %d adalah %d" % (mulai, batas-1, total)
pesan2 = "Rerata nilai penjumlahan %d s.d %d adalah %f" % (mulai, batas-1, rerata)

print(pesan1)
print(pesan2)