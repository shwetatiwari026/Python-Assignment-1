
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))
age = int(input("Enter your age: "))

if salary >= 30000 and credit_score >= 700 and age >= 21 and age <= 60:
    print("Congratulations! Your loan is approved.")

elif (salary >= 30000 and credit_score >= 700) or (salary >= 30000 and age >= 21 and age <= 60) or (credit_score >= 700 and age >= 21 and age <= 60):
    print("Your loan is conditionally approved.")

else:
    print("Loan status: Rejected")

