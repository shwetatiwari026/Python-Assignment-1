subjects = ("Python", "Java", "DBMS", "Maths", "English")

print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))

chosen_subject = input("Enter a subject name to find its index: ")
if chosen_subject in subjects:
    print("Index:", subjects.index(chosen_subject))
else:
    print("That subject is not in the tuple.")
