def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]


word = input("Enter a string: ")
print("Reversed string:", reverse_text(word))
