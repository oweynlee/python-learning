def save(expenses):
    with open ("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

def load():
    expenses = []
    try:
        with open ("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expense = {"category":category,
                    "amount":float(amount)}
            expenses.append(expense)
            
    except FileNotFoundError:
        print("No previous expense file found.")
        print("Starting a new expense tracker.")
    
    return expenses