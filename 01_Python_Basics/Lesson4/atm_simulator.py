def show_balance(balance_amount):
     print(f"Current Balance: RM {balance_amount:.2f}")

def deposit(balance, deposit_amount):
    print(f"\nDeposit Amount: RM {deposit_amount:.2f}")
    print ("Deposit Successful!")
    balance = balance + deposit_amount
    print (f"Current Balance: RM {balance:.2f}")
    return balance

def withdraw(balance, withdraw_amount):
    print(f"\nWithdraw Amount: RM {withdraw_amount:.2f}")
    print ("Withdraw Successful!")
    balance = balance - withdraw_amount
    print (f"Current Balance: RM {balance:.2f}")
    return balance

def exit_program():
    print ("Thank you for using our ATM!")

def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(f"{balance}\n")

def load_balance():
    try: 
        with open("balance.txt", "r") as file:
            balance = float(file.read().strip())
    except FileNotFoundError:
        print("No previous balance file found.")
        print("Starting a new ATM session.")
        balance = 0
        save_balance(balance)
    return balance

balance = load_balance()

while True:
    print("====== ATM ======")

    print ("1. Show Balance", "\n2. Deposit", "\n3. Withdraw", "\n4. Exit")

    decision = int(input("Please select the mode you want to proceed (1-4): "))

    if decision == 1:
        show_balance(balance)

    elif decision == 2:
        deposit_amount = float(input("Please enter deposit amount: RM"))
        balance = deposit(balance, deposit_amount)
        save_balance(balance)

    elif decision == 3:
        withdraw_amount = float(input("Please enter withdraw amount: RM"))
        balance = withdraw(balance, withdraw_amount)
        save_balance(balance)
    else:
        exit_program()
        break








