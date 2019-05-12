import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

filename = 'file.txt'
s.sendall(bytes('%s\n' %(filename), encoding='utf-8'))

pesan = open(filename, 'rb')
for line in pesan.readlines() :
    s.sendall(line)

data = s.recv(102400)
print('File %s Berhasil Terkirim' %(filename))

pesan.close()
s.close()