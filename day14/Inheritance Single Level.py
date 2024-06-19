class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pelajar(Manusia):
    def __init__(self, nama, umur, kelas):
        super().__init__(nama, umur)
        self.kelas = kelas

    def info(self):
        super().info()
        print(f"Kelas: {self.kelas}")

# Contoh penggunaan
p1 = Pelajar("Andi", 17, "12A")
p1.info()
