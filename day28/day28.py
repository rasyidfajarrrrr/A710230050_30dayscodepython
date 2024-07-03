class Employee:
    def __init__(self, name, age, salary):
        # Atribut privat
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Metode untuk mengatur nama
    def set_name(self, name):
        self.__name = name

    # Metode untuk mengambil nama
    def get_name(self):
        return self.__name

    # Metode untuk mengatur usia
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Umur tidak valid")

    # Metode untuk mengambil usia
    def get_age(self):
        return self.__age

    # Metode untuk mengatur gaji
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Gaji tidak valid")

    # Metode untuk mengambil gaji
    def get_salary(self):
        return self.__salary

# Implementasi objek berdasarkan class Employee
employee1 = Employee("Rasyid", 25, 50000)

# Menggunakan metode get untuk mengambil nilai
print("Nama:", employee1.get_name())
print("Usia:", employee1.get_age())
print("Gaji:", employee1.get_salary())

# Menggunakan metode set untuk mengubah nilai
employee1.set_name("Rasyid")
employee1.set_age(30)
employee1.set_salary(60000)

# Menggunakan metode get untuk mengambil nilai yang telah diubah
print("\nNilai yang telah diubah:")
print("Nama:", employee1.get_name())
print("Usia:", employee1.get_age())
print("Gaji:", employee1.get_salary())
