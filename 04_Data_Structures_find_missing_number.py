numbers = list(map(int, input("Enter numbers from 1 to n with one missing: ").split()))
n = int(input("Enter n (the highest number in the range): "))

expected_total = n * (n + 1) // 2
actual_total = 0
for number in numbers:
    actual_total += number

missing = expected_total - actual_total
print("Missing number:", missing)
