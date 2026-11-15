import random

otp = random.randint(100000, 999999)
print("Demo OTP:", otp)

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for _ in range(10):
    password += random.choice(characters)
print("Random demo password:", password)

count = int(input("How many random numbers do you want? "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if count < 0 or low > high:
    print("Please enter valid limits and a non-negative count.")
else:
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(low, high))
    print("Random list:", random_numbers)
