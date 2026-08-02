from tracker import ExpenseTracker
from file_manager import load, save

tracker = ExpenseTracker()
tracker.expenses = load()
options = ["Add Expense", "View Expenses", "Total Expenses", "Delet Expenses", "Exit"]


while True:
    print ("===== Expense Tracker =====")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    decisions = int(input("Choose an option to proceed (1-5):"))

    if decisions == 1:
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: RM"))
        tracker.add(category, amount)
        print("Added Successfully!")
        save(tracker.expenses)
        print("Save Successfully!")


    elif decisions == 2:
        if not tracker.expenses:
            print("No expenses recorded yet.")
        else:
            print(tracker.expenses)
            tracker.view()
    
    
    elif decisions == 3:
        total=tracker.total() 
        print(f"Total Expenses: RM {total:.2f}")
    
    
    elif decisions == 4:
        tracker.view()
        index = int(input("Choose expense number: "))
        tracker.delet(index)
        save(tracker.expenses)
    
    
    else:
        save(tracker.expenses)
        print("Save Successfully!") 
        print("Thank you for using Expense Tracker!")
        break
