balance = float(input("Enter current account balance: "))
amount = float(input("Enter withdrawal amount: "))

try:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Withdrawal amount exceeds the available balance.")
    balance -= amount
    print("Withdrawal successful.")
    print(f"Remaining balance: Rs. {balance:.2f}")
except ValueError as error:
    print("Transaction failed:", error)
