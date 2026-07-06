def save(expenses):
    
    with open("expenses.txt", "w") as file:
        
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")
    
    print("Saving expenses...")

def load():
    pass