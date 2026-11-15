sentence = input("Enter a sentence: ")
words = sentence.split()

if not words:
    print("You did not enter any words.")
else:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("Longest word:", longest)
    print("Length:", len(longest))
