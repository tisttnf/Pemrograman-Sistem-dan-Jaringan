# Program Client
# Mengirim pesan secara broadcast

# Contoh Penggunaan : 
# $ python bclient.py "checkin:1616:Tuti"
# $ python bclient.py "checkout:1616:Tuti"

from socket import *
import sys

if len(sys.argv) < 2 :
    print("Missing 1 argument message")
    sys.exit()

msg = sys.argv[1]

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
maxsize = 1024
BADDRESS = ('10.107.104.98', 10000)
s.sendto(msg.encode(), BADDRESS)
s.close()

# Broadcast : 10.107.255.255
# Broadcast : 10.107.127.255
# 10.0.3.255 : Dosen
# 10.107.241.170 : Azhar
# 10.107.104.98 : Iyan
# checkin:nim:nama
# checkout:nim:nama