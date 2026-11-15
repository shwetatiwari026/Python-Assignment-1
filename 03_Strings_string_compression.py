text = input("Enter a string: ")

if text == "":
    print("Compressed string: ")
else:
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)
    print("Compressed string:", compressed)

# Note: the sheet's example says aaaabbc -> a3b2c1.
# Actually aaaabbc contains four 'a' characters, so this code correctly gives a4b2c1.
