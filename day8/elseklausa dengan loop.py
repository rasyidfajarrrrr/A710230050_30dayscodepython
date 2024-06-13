# Get a number to test from the user, and set the initial divisor to 2
dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break

    # Increment the divisor for the next iteration
    divisor = divisor + 1
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")
