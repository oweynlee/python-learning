class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
    def add(self, category, amount):
        expense = {
            "category": category,
            "amount": amount
        }
        self.expenses.append(expense)
    def view(self):
        if not self.expenses:
             print("No expenses recorded yet.")
        else:
            for index, expense in enumerate(self.expenses, start=1):
                print(f"{index}. Category: {expense['category']}, Amount: RM {expense['amount']:.2f}")

    
    def view_total(self):
        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        return total
    
    def delete(self, index):

        if 1 <= index <= len(self.expenses):
            self.expenses.pop(index - 1)
            print("Deleted Successfully!")
        else:
            print("Invalid expense number.")
    
tracker = ExpenseTracker()
tracker.add("Food",20)
tracker.view()
print(tracker.expenses) 
print(f"Total expenses: RM {tracker.view_total():.2f}")
