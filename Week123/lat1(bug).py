total = 0
rerata = 0
counter = 0

mulai = int(input("Masukan awal: "))
batas = int(input("Masukan batas: "))

for x in range(mulai,batas):
    total = total + x
    counter += 1

rerata = total/counter

pesan1 = "Total nilai penjumlahan %d s.d %d adalah %d" % (mulai,batas-1,total)
pesan2 = "Rerata nilai penjumlahan %d s.d %d adalah %d" % (mulai,batas-1,rerata)

print(pesan1)
print(pesan2)