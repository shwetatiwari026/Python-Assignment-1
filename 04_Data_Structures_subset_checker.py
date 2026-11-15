first_set = set(input("Enter elements of the first set: ").split())
second_set = set(input("Enter elements of the second set: ").split())

if first_set.issubset(second_set):
    print("The first set is a subset of the second set.")
else:
    print("The first set is not a subset of the second set.")
