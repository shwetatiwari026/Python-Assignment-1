values = (10, 20, 30, 40, 50)

if len(values) >= 2:
    first, *middle, last = values
    swapped = (last, *middle, first)
    print("Original tuple:", values)
    print("After swapping first and last:", swapped)
else:
    print("The tuple needs at least two elements.")
