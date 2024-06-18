class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# membuat objek calculator
my_calculator = Calculator()

# memanggil method add dengan dua parameter
result1 = my_calculator.add(2, 3)
print(result1) # output: 5

# memanggil method add dengan tiga parameter
result2 = my_calculator.add(2, 3, 4)
print(result2) # output: 9
