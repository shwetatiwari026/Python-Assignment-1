import math

number = float(input("Enter a number: "))
exponent = float(input("Enter power: "))
angle = float(input("Enter angle in degrees for trigonometry: "))

if number < 0:
    print("Square root: not available for a negative number in real numbers.")
else:
    print("Square root:", math.sqrt(number))

print("Power:", math.pow(number, exponent))
if number >= 0 and number.is_integer():
    print("Factorial:", math.factorial(int(number)))
else:
    print("Factorial: enter a non-negative whole number to calculate it.")

radians = math.radians(angle)
print("Sine:", math.sin(radians))
print("Cosine:", math.cos(radians))
print("Tangent:", math.tan(radians))
