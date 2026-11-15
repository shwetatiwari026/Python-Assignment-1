def factorial(number):
    if number < 0:
        return None

    answer = 1
    for value in range(1, number + 1):
        answer *= value
    return answer


n = int(input("Enter a non-negative integer: "))
result = factorial(n)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is {result}.")
