
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = float(input("Enter subject marks: "))
        marks.append(mark)

    students[name] = marks

if n == 0:
    print("No student records found.")

else:
    highest = 0
    topper = ""

    total = 0
    count = 0

    for name in students:
        average = sum(students[name]) / 3

        if average > highest:
            highest = average
            topper = name

        for mark in students[name]:
            total = total + mark
            count = count + 1

    print("Class topper:", topper)
    print("Class average:", round(total / count, 2))

    print("Students who failed:")

    for name in students:
        for mark in students[name]:
            if mark < 33:
                print(name)
                break
