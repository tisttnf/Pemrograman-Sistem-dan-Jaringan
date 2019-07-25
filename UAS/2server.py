# Server listen on port 9000/udp
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 9000))
while True:
    data, addr = s.recvfrom(1024)
    if not data:
        continue
    print('Connection from', addr, " Data: ",data)


