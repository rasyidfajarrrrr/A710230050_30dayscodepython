import random

angka_rahasia = random.randint(1, 10)
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (antara 1 dan 10): "))
    if tebakan < angka_rahasia:
        print("Terlalu rendah!")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi!")
    else:
        print("Selamat, tebakan Anda benar!")
