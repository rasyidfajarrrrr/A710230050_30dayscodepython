# Kelas Induk
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}")

# Kelas Anak
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance is {self.balance}")

# Membuat objek
savings = SavingsAccount("John Doe", 1000, 0.05)

# Menggunakan metode dari kelas induk
savings.deposit(500)
savings.withdraw(200)

# Menggunakan metode dari kelas anak
savings.add_interest()
# Output:
# 500 deposited. New balance is 1500
# 200 withdrawn. New balance is 1300
# Interest added: 65.0. New balance is 1365.0
