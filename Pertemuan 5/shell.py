import os

cmd = "df -h /"
os.system(cmd)
res = os.system(cmd)
# Jika res = 0 maka berhasil
print(res)

cmd = "df -h /asdjk"
res = os.system(cmd)
# Jika res != 0 maka gagal
print(res)

cmd = "df -h /"
res = os.popen(cmd)
# popen() untuk membaca shell namun hanya 1x
print(res.read())
print(res.read())

cmd = "free -m"
res = os.popen(cmd)
print(res.read()) # Berupa string
res = os.popen(cmd)
print(res.readlines()) # Berupa list

# popen untuk menyimpan command ke dalam sebuah variable
cmd = "df -h /"
res = os.popen(cmd)
output1 = res.read()
print(output1)

res2 = os.popen(cmd)
output2 = res2.readlines()
print(output2)