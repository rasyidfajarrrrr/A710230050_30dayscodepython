def maks(a):
    m = a[0]
    for i in a:
        if m < i:
            m = i

    return m

print(maks([5, 2, 1, 4]))