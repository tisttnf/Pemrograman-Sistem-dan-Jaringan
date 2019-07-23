# Unicast Server dan Multicast Client
from socket import *
import struct
import sys
import os

s = socket(AF_INET,SOCK_DGRAM)
s.bind( ("", 20000) )
maxsize = 1024
while True:
    os.system("clear")
    print("======")
    print("|X-PC|")
    print("======")
    print("\nMenunggu Pesan dari Y-PC...")
    data, addr = s.recvfrom(maxsize)
    
    resp = "Pesan Berhasil diKirim ke X-PC"
    s.sendto(resp.encode(), addr)
    print(f"\nPesan dari Y-PC : {data.decode()}")    
    input("\nTekan Enter Untuk Forward Pesan...")    

    pesan = data.decode()
    ip = '224.3.29.71'
    port = 10000            

    multicast_group = (ip, port)

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.settimeout(0.2)
    ttl = struct.pack('b', 3)
    sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)

    try:
        print("\n===== Forward =====")
        print(f"Pesan : {pesan}")       
        print(f"IP : {ip}")
        print(f"Port : {port}")
        print("===================")
        sent = sock.sendto(pesan.encode(), multicast_group)

        while True:            
            try:
                data, server = sock.recvfrom(16)
            except timeout:                
                break
            else:
                break
    finally:        
        sock.close()
        input("\nTekan Enter Untuk Menerima Pesan Lagi...")            