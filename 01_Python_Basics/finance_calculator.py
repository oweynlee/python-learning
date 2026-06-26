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

if 10 < saving_rate < 30:
    print("Good job!Keep improving.")

if saving_rate < 10:
    print("Consider reducing your expenses.")



    


# ---------------------------------------- #
Name = "Oweyn"
Dream_Company = "JPMorgan"
Favourite_Stock = "TSLA"

print(Name, Dream_Company, Favourite_Stock)

Age = int(input("What is your age? "))
Height = float(input("What is your height in meters? "))

print("Age:", Age)
print("Height:", Height, "meters")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division::", a/b)