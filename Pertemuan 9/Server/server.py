import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

pesan = open('file.txt', 'wb')

while True:
    conn, addr = s.accept()
    print('Connected by', addr)

    data = conn.recv(1024)    
    pesan.write(data)
    print("File diterima ke dalam file.txt")

    conn.sendall(data) 
    if not data :        
        continue
    else :
        break    
        
pesan.close()
s.close()