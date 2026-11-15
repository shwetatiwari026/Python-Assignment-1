# A small dictionary-based library record: book name -> available quantity.
library = {"Python Basics": 3, "Learning Java": 2}

while True:
    print("\\n1. Show books  2. Add/update book  3. Issue book  4. Return book  5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        if library:
            for book, quantity in library.items():
                print(book, ":", quantity)
        else:
            print("The library is empty.")

    elif choice == "2":
        book = input("Enter book name: ")
        quantity = int(input("Enter quantity to add: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
        else:
            library[book] = library.get(book, 0) + quantity
            print("Book quantity updated.")

    elif choice == "3":
        book = input("Enter book name to issue: ")
        if library.get(book, 0) > 0:
            library[book] -= 1
            print("Book issued.")
        else:
            print("Book is not available.")

    elif choice == "4":
        book = input("Enter book name to return: ")
        library[book] = library.get(book, 0) + 1
        print("Book returned.")

    elif choice == "5":
        print("Library program closed.")
        break

    else:
        print("Please enter a valid option.")
