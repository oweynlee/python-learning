print ("=== Monthly Savings Calculator ===")

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

savings = income - expenses
saving_rate = (savings/income)*100

print()
print("Monthly Income: RM", income)
print("Monthly Expenses: RM", expenses)
print("Monthly Savings: RM", savings)
print(f"Savings Rate: {saving_rate:.2f}%")

if saving_rate > 30:
    print("Great job! Excellent savings habit.")
elif 10 < saving_rate < 30:
    print("Good job!Keep improving.")
else:
    print("Consider reducing your expenses.")



