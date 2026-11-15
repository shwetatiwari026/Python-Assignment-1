first = input("Enter the first string: ")
second = input("Enter the second string: ")

# Ignore spaces and letter case before comparing.
first_clean = first.replace(" ", "").lower()
second_clean = second.replace(" ", "").lower()

if sorted(first_clean) == sorted(second_clean):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
