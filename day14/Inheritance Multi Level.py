class Kendaraan:
    def __init__(self, jenis):
        self.jenis = jenis

class Sepeda(Kendaraan):
    def __init__(self, jenis, warna):
        super().__init__(jenis)
        self.warna = warna

class SepedaMotor(Sepeda):
    def __init__(self, jenis, warna, merk):
        super().__init__(jenis, warna)
        self.merk = merk

# Contoh penggunaan
sm = SepedaMotor("Motor", "Merah", "Honda")
print(f"Jenis: {sm.jenis}, Warna: {sm.warna}, Merk: {sm.merk}")
