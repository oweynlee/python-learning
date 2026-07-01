expenses = []
choices = ["Add Expense", "View Expenses", "Total Expenses", "Exit"]


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
    

while True:
    print ("===== Expense Tracker =====")

    for _, choice in zip(range(1, 5), choices):
        print(f"{_}. {choice}")

    decisions = int(input("Please select the mode you want to proceed (1-4):"))

    if decisions == 1:
        add()
        print("Added Successfully!")
    elif decisions == 2:
        view()
        if expenses == []:
            print("No expenses recorded yet.")
    elif decisions == 3:
        total=total_view()
        if total == 0:
            print("No expenses recorded yet.")
        else:
            print(f"\nTotal Expenses: RM {total:.2f}")   
    else:
        exit()
        break
