def main():
    # Menerima jumlah barang
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    # Inisialisasi variabel untuk menyimpan total harga dan rincian belanja
    total_harga = 0
    rincian_belanja = []

    # Loop untuk menerima harga setiap barang
    for i in range(jumlah_barang):
        nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
        harga_barang = float(input(f"Masukkan harga {nama_barang}: "))
        total_harga += harga_barang
        rincian_belanja.append(f"{nama_barang}: Rp{harga_barang}")

    # Menampilkan total harga
    print("\nTotal harga belanja: Rp", total_harga)

    # Menyimpan rincian belanja ke file invoice.txt
    with open("invoice.txt", "w") as file:
        file.write("Rincian Belanja:\n")
        for item in rincian_belanja:
            file.write(item + "\n")
        file.write("\nTotal harga belanja: Rp" + str(total_harga))

    print("\nInvoice telah dibuat dan disimpan sebagai 'invoice.txt'.")

if __name__ == "__main__":
    main()
