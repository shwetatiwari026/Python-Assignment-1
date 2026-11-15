from datetime import datetime, date

now = datetime.now()
print("Current date:", now.strftime("%d-%m-%Y"))
print("Current time:", now.strftime("%I:%M:%S %p"))

birth_text = input("Enter your date of birth (DD-MM-YYYY): ")
try:
    birth_date = datetime.strptime(birth_text, "%d-%m-%Y").date()
    today = date.today()

    if birth_date > today:
        print("Date of birth cannot be in the future.")
    else:
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        print("Your age is:", age)
except ValueError:
    print("Please enter the date in DD-MM-YYYY format.")
