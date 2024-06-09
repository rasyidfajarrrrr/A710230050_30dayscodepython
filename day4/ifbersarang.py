a, b, c = input('Masukkan 3 angka tanpa spasi: ')
if a > b:
    if b > c:
        maks = a
    else:
        if c > a:
            maks = c
elif a > c:
    maks = b
elif c > b:
    maks = c


print(maks)