from socket import socket, AF_INET, SOCK_STREAM
(SERVER, PORT) = ('127.0.0.1', 8888)
s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER, PORT))
s.send(b'Halo Dunia')
data = s.recv(1024)
s.close()
print('Received', data)