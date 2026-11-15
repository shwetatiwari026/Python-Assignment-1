class PasswordValidationError(Exception):
    pass


password = input("Create a password: ")

try:
    if len(password) < 8:
        raise PasswordValidationError("Password must contain at least 8 characters.")
    if not any(character.isupper() for character in password):
        raise PasswordValidationError("Password must contain at least one uppercase letter.")
    if not any(character.isdigit() for character in password):
        raise PasswordValidationError("Password must contain at least one number.")

    print("Password accepted.")
except PasswordValidationError as error:
    print("Password error:", error)
