from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
print("using", s.getsockname())
server = ('127.0.0.1', 9000)

message = input('Masukkan pesan: ')
s.sendto(message.encode(), (server))

s.close()