# Kelas Induk
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Kelas Anak
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Memanggil konstruktor kelas induk
        self.employee_id = employee_id

    def info(self):
        super().info()  # Memanggil metode info dari kelas induk
        print(f"Employee ID: {self.employee_id}")

# Membuat objek
emp = Employee("Alice", 30, "E1234")

# Memanggil metode info
emp.info()
# Output:
# Name: Alice, Age: 30
# Employee ID: E1234
