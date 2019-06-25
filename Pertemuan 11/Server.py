from socket import *
import os

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(("",10000))
maxsize = 1024
db = {}

while True:
    message, addr = s.recvfrom(maxsize)
    data = message.decode()
    strdata = data.split(":")
    cmd = strdata[0]
    nim = strdata[1]
    nama = strdata[2]

    if cmd == "checkin" :
        db[nim] = nama
    elif cmd == "checkout" :
        db.pop(nim)
    else :
        pass

    os.system("clear")

    print("Students in Lab")

    for x in db :
        print("%s - %s" %(x, db[x]))