balance = 0

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

while True:
    print("====== ATM ======")

    print ("1. Show Balance", "\n2. Deposit", "\n3. Withdraw", "\n4. Exit")

    decision = int(input("Please select the mode you want to proceed (1-4): "))

    if decision == 1:
        show_balance(balance)

    elif decision == 2:
        deposit_amount = float(input("Please enter deposit amount: RM"))
        balance = deposit(balance, deposit_amount)

    elif decision == 3:
        withdraw_amount = float(input("Please enter withdraw amount: RM"))
        balance = withdraw(balance, withdraw_amount)
    else:
        exit_program()
        break








