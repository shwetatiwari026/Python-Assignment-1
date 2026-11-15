start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Palindrome numbers:")
for number in range(start, end + 1):
    if str(number) == str(number)[::-1]:
        print(number, end=" ")
print()
