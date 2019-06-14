from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind( ("",10000) )
maxsize = 1024
while True:
    data, addr = s.recvfrom(maxsize)
    resp = "Get off my lawn!"
    s.sendto(resp.encode(),addr)
    print(data.decode())