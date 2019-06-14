import socket

HOST = '127.0.0.1'
PORT = 65432

# 1. Membuat Socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Menetapkan socket address
s.bind((HOST, PORT))

# 3. Socket mendengarkan permintaan (listening)
s.listen()

while True:
    # 4. Menerima koneksi baru
    conn, addr = s.accept()
    print('Connected by', addr)

    if addr :
        # 5. Membuat variabel LIST untuk menampung urutan pesan/data
        fragments = []

        while True :
            # 6. Menerima pesan/data
            data = conn.recv(1024)   
            if not data :        
                break     

            # 7. Menambahkan data/pesan yang diterima ke LIST
            fragments.append(data.decode())

        # 8. Menutup koneksi
        conn.close()

        # 9. Mengambil data nama file dari LIST
        fname = fragments.pop(0)

        # 10. Menggabungkan item item LIST menjadi string pesan
        message = "".join(fragments)

        # 11. Membuka dan membuat file baru
        f = open(fname, 'w')
        
        # 12. Menuliskan pesan string ke file
        f.write(message)

        f.close()
    else :
        continue