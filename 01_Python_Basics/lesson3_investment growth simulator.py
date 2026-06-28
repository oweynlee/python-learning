invesment = float(input("Please enter your initial invesment amount: RM "))

annual_return = float(input("Please enter your annial return: "))

years = int(input("Please enter your year of invesment: "))

print(f"\nInvesment: RM {invesment:.2f}")

for year in range(1,years+1):
    invesment = invesment*(1+annual_return/100)
    print("Year", year, f": RM {invesment:.2f}")

 


 

