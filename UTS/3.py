import os

ip = input("Masukan Alamat IP atau Nama Host : ")
status = "Down"
cmd = os.popen("ping -qc3 %s" %(ip))
cek = cmd.read()
print(cek)
if cek.find("3 received") > -1 :
    status = "Up"

print("Host %s is %s" %(ip,status))