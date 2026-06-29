principal = float(input("Please enter your initial invesment amount: RM "))
rate = float(input("Please enter your annial return: "))
years = int(input("Please enter your year of invesment: "))

def compound_interest(principal, rate, years):

    for _ in range(1,years+1):
        principal = principal*(1+rate/100)
    return (principal)

result = compound_interest(principal, rate, years)
print(f"Final Amount: RM {result:.2f}")