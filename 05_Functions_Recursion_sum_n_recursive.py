def sum_n(number):
    if number <= 0:
        return 0
    return number + sum_n(number - 1)


n = int(input("Enter a positive integer: "))
if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Sum of first", n, "natural numbers is", sum_n(n))
