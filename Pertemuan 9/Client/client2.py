import socket

HOST = '127.0.0.1'
PORT = 65432

# 1. Membuat Socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Menghubungi server
s.connect((HOST, PORT))
fname = 'data.txt'

# 3. Membuka file
f = open(fname)

# 4. Mengirimkan pesan berupa Nama File
s.send(fname.encode())

# 5. Membaca baris baris file
for line in f.readlines() :
    # 6. Mengirimkan data baris fila yang dibaca ke server
    s.sendall(line.encode())
s.close()