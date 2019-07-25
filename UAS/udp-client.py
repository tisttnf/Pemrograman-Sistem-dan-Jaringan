from socket import *
import sys

if len(sys.argv) < 2 :
    print("Missing 1 argument message")
    sys.exit()

s = socket(AF_INET, SOCK_DGRAM)
msg = sys.argv[1]
maxsize = 1024
s.sendto(msg.encode(),("127.0.0.1",10000) )
data, addr = s.recvfrom(maxsize)
print(data)