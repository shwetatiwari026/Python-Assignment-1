def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    return base * power(base, exponent - 1)


base = float(input("Enter the base: "))
exponent = int(input("Enter an integer exponent: "))

if base == 0 and exponent < 0:
    print("Zero cannot have a negative exponent.")
else:
    print("Answer:", power(base, exponent))
