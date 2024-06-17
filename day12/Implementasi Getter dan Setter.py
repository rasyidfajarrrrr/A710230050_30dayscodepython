class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Membuat objek person
person = Person("Abdul Hakim", 25)
print(person.get_name())
print(person.get_age())

# Mengubah nilai variabel name dan age dengan method setter
person.set_name("Ryan Hakim")
person.set_age(30)

print(person.get_name())
print(person.get_age())

# Mengakses private attribute secara langsung (ini akan menghasilkan error)
# print(person.__name) # This line will cause an AttributeError
