# Kelas Induk
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Kelas Anak
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Membuat objek
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Memanggil metode speak
dog.speak()  # Output: Buddy barks
cat.speak()  # Output: Whiskers meows
