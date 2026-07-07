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

