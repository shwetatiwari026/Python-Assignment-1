number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    square = number * number
    digits = len(str(number))

    if square % (10 ** digits) == number:
        print(f"{number} is an automorphic number.")
    else:
        print(f"{number} is not an automorphic number.")

    print(f"Square: {square}")
