class ATM:
    def __init__(self, pin, balance):
        self.__pin = str(pin)
        self.__balance = balance

    def check_pin(self, entered_pin):
        return self.__pin == str(entered_pin)

    def show_balance(self, entered_pin):
        if self.check_pin(entered_pin):
            print(f"Available balance: Rs. {self.__balance:.2f}")
        else:
            print("Incorrect PIN.")

    def withdraw(self, entered_pin, amount):
        if not self.check_pin(entered_pin):
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Please collect your cash.")
            print(f"Remaining balance: Rs. {self.__balance:.2f}")


atm = ATM("1234", 5000)
pin = input("Enter your demo PIN: ")
atm.show_balance(pin)

amount = float(input("Enter withdrawal amount: "))
atm.withdraw(pin, amount)
