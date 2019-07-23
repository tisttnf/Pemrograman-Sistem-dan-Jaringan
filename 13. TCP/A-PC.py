from socket import *
import struct
import sys
import os

multicast_group = '224.3.29.71'
server_address = ('', 10000)
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(server_address)
group = inet_aton(multicast_group)
mreq = struct.pack('4sL', group, INADDR_ANY)
sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

while True:
    os.system("clear")
    print("======")
    print("|A-PC|")
    print("======")
    print('\nMenunggu Pesan dari X-PC...')
    data, address = sock.recvfrom(1024)
    
    print(f'\nPesan dari X-PC : {data}')
    print(f'Dari IP : {address}')

    sock.sendto(b'ACK', address)
    input("\nTekan Enter Untuk Menerima Pesan Lagi...")