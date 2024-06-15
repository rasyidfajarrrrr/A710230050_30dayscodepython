class Dog:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def duduk(self):
        print(f"{self.nama} sekarang duduk")

    def berdiri(self):
        print(f"{self.nama} sekarang berdiri")

my_dog = Dog("Wili", 6)

print(f"Anjingku bernama {my_dog.nama}")
print(f"Anjingku berumur {my_dog.umur} tahun")

my_dog.duduk()
my_dog.berdiri()
