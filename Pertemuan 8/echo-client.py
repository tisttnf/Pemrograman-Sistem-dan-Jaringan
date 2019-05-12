import socket
HOST = '127.0.0.1'
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
pesan = 'Hello World'
s.sendall(pesan.encode())
data = s.recv(1024)
print('Received', data.decode())
