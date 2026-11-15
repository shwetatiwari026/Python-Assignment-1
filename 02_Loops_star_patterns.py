rows = int(input("Enter number of rows: "))

print("\\nTriangle:")
for i in range(1, rows + 1):
    print("* " * i)

print("\\nPyramid:")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)

print("\\nDiamond:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
