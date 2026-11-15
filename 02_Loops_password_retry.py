correct_password = "python123"  # Demo password; change it for your own practice.
attempts = 0
maximum_attempts = 3

while attempts < maximum_attempts:
    entered_password = input("Enter password: ")

    if entered_password == correct_password:
        print("Login successful.")
        break

    attempts += 1
    remaining = maximum_attempts - attempts
    if remaining > 0:
        print(f"Incorrect password. {remaining} attempt(s) left.")
    else:
        print("Too many failed attempts. Account blocked.")
