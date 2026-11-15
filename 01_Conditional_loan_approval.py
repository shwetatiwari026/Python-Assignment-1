salary = float(input("Enter monthly salary in rupees: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

salary_ok = salary >= 30000
credit_ok = credit_score >= 700
age_ok = 21 <= age <= 60

conditions_met = sum([salary_ok, credit_ok, age_ok])

if conditions_met == 3:
    print("Loan status: Approved")
elif conditions_met == 2:
    print("Loan status: Conditionally Approved")
else:
    print("Loan status: Rejected")

# The assignment does not define the conditional-approval rule.
# This solution uses 2 out of 3 conditions as conditional approval.
