from tracker import ExpenseTracker
from file_manager import save

tracker = ExpenseTracker()

tracker.add("Food", 20)
tracker.add("Coffee", 8)

tracker.view()
save(tracker.expenses)

print("Total expenses:", tracker.count())