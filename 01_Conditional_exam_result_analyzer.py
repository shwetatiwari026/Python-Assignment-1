
marks = []

for i in range(1, 6):
    marks.append(float(input("Enter your marks: ")))

if any(m < 0 or m > 100 for m in marks):
    print("Please enter valid marks between 0 and 100.")

elif any(m < 33 for m in marks):
    print("Sorry, you are fail because you scored less than 33 in a subject.")

else:
    average = sum(marks) / 5

    print("Your average marks are:", round(average, 2))

    if average >= 60:
        print("You got First Division!")

    elif average >= 50:
        print("You got Second Division!")

    elif average >= 40:
        print("You got Third Division!")

    else:
        print("You passed!")
