
counter = 0
total = 0

jumlah_barang = int(input('Masukkan Jumlah Barang : '))
while counter < jumlah_barang:
    harga = int(input('Masukkan harga barang ke-{}: '.format(counter+1)))
    jumlah = int(input('Masukkan jumlah barang ke-{}: '.format(counter+1)))
    total = total + (harga*jumlah)
    counter = counter+1

print('Total Harga Barang :',total)