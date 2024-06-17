class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# akses nilai variabel salary secara langsung
print(oPerson1.salary)
print(oPerson2.salary)

# mengubah nilai variabel salary secara langsung
oPerson1.salary = 100000
oPerson2.salary = 111111

print(oPerson1.salary)
print(oPerson2.salary)
