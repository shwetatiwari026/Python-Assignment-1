sentence = input("Enter a string: ")

cleaned = sentence.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
