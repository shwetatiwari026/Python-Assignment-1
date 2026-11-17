num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    square = num * num
    digits = len(str(num))

    if square % (10 ** digits) == num:
        print(f"{num} is an automorphic number.")
    else:
        print(f"{num} is not an automorphic number.")

    print(f"Square: {square}")
