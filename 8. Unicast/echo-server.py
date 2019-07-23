import socket
HOST = '127.0.0.1'
# address (localhost)
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    if not data:
        continue    
    print("Pesan : ", data.decode()) # Tambahan
    conn.sendall(data)