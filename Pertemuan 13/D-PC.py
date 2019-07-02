from socket import *
import struct
import sys
import os

multicast_group = '224.3.29.71'
server_address = ('', 30000)

# Create the socket
sock = socket(AF_INET, SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = inet_aton(multicast_group)
mreq = struct.pack('4sL', group, INADDR_ANY)
sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
# Receive/respond loop
while True:
    os.system("clear")
    print("======")
    print("|D-PC|")
    print("======")
    print('\nMenunggu Pesan dari X-PC...')
    data, address = sock.recvfrom(1024)
    
    print(f'\nPesan dari X-PC : {data}')
    print(f'Dari IP : {address}')

    sock.sendto(b'ACK', address)
    input("\nTekan Enter Untuk Menerima Pesan Lagi...")