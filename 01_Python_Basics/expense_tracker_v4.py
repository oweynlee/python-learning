def add():
    category = input("Please enter your expense category: ")
    amount = float(input("Please enter your expense: RM "))
    expense = {"category": category, "amount": amount}
    expenses.append(expense)

def view():
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Category: {expense["category"]}, Amount: RM {expense["amount"]:.2f}")

def total_view():   
    total = 0                        #OUTSIDE OF LOOP BUT LOCAL NOT GLOBAL VARIABLE
    for expense in expenses:
        total = total + expense["amount"]
    return total

def exit():
    print("Thank you for using the expense tracker!")

def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense["category"]},{expense["amount"]}\n")

def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for expense in file:
                category, amount = expense.strip().split(",")
                expense = {"category":category,
                        "amount":float(amount)}
                expenses.append(expense)
    except FileNotFoundError:
        print("No previous expense file found.")
        print("Starting a new expense tracker.")
        save_expenses()  

expenses = []
options = ["Add Expense", "View Expenses", "Total Expenses", "Exit"]
load_expenses()

while True:
    print ("===== Expense Tracker =====")

    for index, options in enumerate(options, start=1):
        print(f"{index}. {options}")

    decisions = int(input("Choose an option to proceed (1-4):"))

    if decisions == 1:
        add()
        print("Added Successfully!")
        save_expenses()
    elif decisions == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            view()
    elif decisions == 3:
        total=total_view()
        if total == 0:
            print("No expenses recorded yet.")
        else:
            print(f"\nTotal Expenses: RM {total:.2f}")   
    else:
        exit()
        break
