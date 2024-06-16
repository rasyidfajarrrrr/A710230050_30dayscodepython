try:
    # blok kode yang mungkin menimbulkan exception
    num1 = int(input("Masukkan angka pertama: "))
    num2 = int(input("Masukkan angka kedua: "))
    hasil = num1 / num2
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    # exception handler untuk nilai yang tidak valid
    print("Input harus berupa angka!")
except ZeroDivisionError:
    # exception handler untuk pembagian dengan nol
    print("Tidak bisa melakukan pembagian dengan nol!")
except Exception as e:
    # exception handler umum
    print(f"Terjadi kesalahan: {e}")
finally:
    # blok kode yang akan selalu dijalankan
    print("Program selesai.")
