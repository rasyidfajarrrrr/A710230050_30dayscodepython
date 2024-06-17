class Person:
    def __init__(self, name, salary):
        self.__name = name # variabel private
        self.__salary = salary # variabel private

    def get_salary(self):
        return self.__salary

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# akses nilai variabel salary menggunakan getter
print(oPerson1.get_salary())
print(oPerson2.get_salary())
