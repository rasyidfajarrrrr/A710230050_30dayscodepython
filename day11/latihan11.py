def get_integer_input():
    while True:
        try:
            user_input = int(input("Masukkan bilangan bulat: "))
            return user_input
        except ValueError:
            print("Input yang dimasukkan tidak valid! Silakan coba lagi.")

def main():
    number = get_integer_input()
    result = number ** 2
    print(f"Hasil pangkat dua dari {number} adalah {result}")

if __name__ == "__main__":
    main()
