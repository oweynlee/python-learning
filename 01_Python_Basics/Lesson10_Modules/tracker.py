class ExpenseTracker:

    def __init__(self):
        self.expenses = []

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
                print(f"{index}. {expense['category']} - RM {expense['amount']:.2f}")

    def count(self):
        return len(self.expenses)