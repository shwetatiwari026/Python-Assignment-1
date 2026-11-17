
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

num1 = abs(a)
num2 = abs(b)

while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

hcf = num1

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // hcf

print("HCF of the numbers is:", hcf)
print("LCM of the numbers is:", lcm)

