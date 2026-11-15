marks = []
for subject in range(1, 6):
    mark = float(input(f"Enter marks for subject {subject} (out of 100): "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Please enter marks between 0 and 100.")
elif any(mark < 33 for mark in marks):
    print("Result: Fail (at least one subject is below 33).")
else:
    average = sum(marks) / 5
    print(f"Average: {average:.2f}%")

    if average >= 60:
        print("Result: First Division")
    elif average >= 50:
        print("Result: Second Division")
    elif average >= 40:
        print("Result: Third Division")
    else:
        print("Result: Pass, but the assignment does not specify a division below 40%.")
