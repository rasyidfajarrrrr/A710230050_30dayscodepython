print("Menghitung Luas dan Keliling Persegi")
#mengambil inputan panjang
panjang = input('Masukkan nilai Panjang: ')

#mengambil inputan lebar
lebar = input ('Masukkan nilai Lebar: ')

#menghitung luas dan keliling
luas = int(panjang) * int(lebar)
keliling = 2 * (int(panjang) + int(lebar))

#menampilkan hasil
print ('Luas Persegi adalah ', luas ,' sedangkan kelilingnya adalah ',
keliling)