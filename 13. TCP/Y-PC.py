from socket import *
import sys
import os

os.system("clear")

s = socket(AF_INET, SOCK_DGRAM)
print("======")
print("|Y-PC|")
print("======")
print()
pesan = input("Ketik Pesan : ")
maxsize = 1024
s.sendto(pesan.encode(), ("192.168.43.186", 20000) )
data, addr = s.recvfrom(maxsize)
print(f"\n{data}")