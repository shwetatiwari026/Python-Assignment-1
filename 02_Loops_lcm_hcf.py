a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find HCF using the Euclidean loop method.
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
hcf = x

# LCM is zero if either input is zero.
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
