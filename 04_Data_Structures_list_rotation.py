numbers = list(map(int, input("Enter list numbers separated by spaces: ").split()))
direction = input("Rotate left or right? ").strip().lower()
k = int(input("Enter number of positions: "))

if numbers:
    k = k % len(numbers)
    if direction == "left":
        rotated = numbers[k:] + numbers[:k]
    elif direction == "right":
        rotated = numbers[-k:] + numbers[:-k] if k != 0 else numbers[:]
    else:
        rotated = None
        print("Please choose left or right.")

    if rotated is not None:
        print("Rotated list:", rotated)
else:
    print("The list is empty.")
