expenses = []
choices = ["Add Expense", "View Expenses", "Total Expenses", "Exit"]


def add():
    value = float(input("Please enter your expense: RM "))
    expenses.append(value)
    return expenses

def view():
    for expense in expenses:
        print(f"RM {expense:.2f}")

def total_view():   
    total = 0                               #OUTSIDE OF LOOP BUT LOCAL NOT GLOBAL VARIABLE
    for expense in expenses:
        total = total + expense
    return total

def exit():
    print("Thank you for using the expense tracker!")
    

while True:
    print ("===== Expense Tracker =====")

    for _, choice in zip(range(1, 5), choices):
        print(f"{_}.{choice}")

    decisions = int(input("Please select the mode you want to proceed (1-4):"))

    if decisions == 1:
        add()
        print("Added Successfully!")
    elif decisions == 2:
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
