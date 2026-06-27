print ("=== Savings Advisor ===")

income =float(input("Monthly Income: RM "))
expenses = float(input("Monthly Expenses: RM "))

savings = income - expenses 
saving_rate = (savings/income)*100

print(f"\nSavings Rate: {saving_rate:.2f}%")

if saving_rate >= 30:
    print("Excellent! You have a strong savings habits")
elif saving_rate >= 10:
    print("Good job! Keep improving.")
else:
    print("Consider reducing your expenses.")

#----------------------------------------- #

## Loan Eligibility Checker

income = float(input("Enter your monthly income:"))
debt = float(input("Enter your monthly debt:"))

debt_ratio=(debt/income)*100

if debt_ratio < 30:
    print("Loan Approved")
elif 30 <=debt_ratio <=50:
    print("Further Review Needed")
else:
    print("Loan Rejected")