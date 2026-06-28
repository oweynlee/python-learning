print ("=== Loan Eligibility Checker ===")


income = float(input("Enter your monthly income:"))
debt = float(input("Enter your monthly debt:"))

debt_ratio=(debt/income)*100
print(f"\nDebt Ratio: {debt_ratio:.2f}%")

if debt_ratio < 30:
    print("Loan Approved")
elif 30 <=debt_ratio <=50:
    print("Further Review Needed")
else:
    print("Loan Rejected")