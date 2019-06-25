while True:
    data = input('Input (q untuk keluar) = ')
    if data == 'q':
        break
    else:
        nama = data[::-1]
        print(nama)
        continue