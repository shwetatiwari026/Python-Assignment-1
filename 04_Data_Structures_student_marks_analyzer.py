students = {}
student_count = int(input("How many students? "))

for i in range(student_count):
    name = input(f"Enter name of student {i + 1}: ")
    marks = list(map(float, input("Enter marks in subjects separated by spaces: ").split()))
    students[name] = marks

if not students:
    print("No student records were entered.")
else:
    topper = max(students, key=lambda name: sum(students[name]) / len(students[name]))
    all_marks = [mark for marks in students.values() for mark in marks]
    average = sum(all_marks) / len(all_marks) if all_marks else 0

    print("Topper:", topper)
    print("Class average of all entered marks:", round(average, 2))
    print("Students with at least one subject below 33:")
    failures = [name for name, marks in students.items() if any(mark < 33 for mark in marks)]
    print(failures if failures else "None")
