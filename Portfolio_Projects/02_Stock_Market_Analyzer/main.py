import numpy as np

companies = ["Apple", "Tesla", "Nvidia"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

prices = np.array([
    [180, 182, 185, 187, 190],
    [240, 238, 245, 247, 250],
    [980, 995, 1010, 1005, 1025]
])

options = ["Show all stock prices",
           "Average price of each company",
           "Highest stock price",
           "Lowest stock price",
           "Increase all prices by %",
           "Show one company's prices",
           "Show one day's prices",
           "Exit"
]


while True:
    print("========== Stock Market Analyzer ==========")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    choice = int(input("Enter your choice: "))

    if choice > 8:
        print("Option invalid please select again.")
        choice = int(input("Enter your choice : "))

    elif choice == 1:
        for index, company in enumerate(companies):
            print(f"\n{company} ")
            for day_index,day in enumerate(days):
                print(f"{day:<10}: RM {prices[index][day_index]:.2f}")

    elif choice == 2:
        print("Average Stock Price")
        averages = np.mean(prices, axis=1)
        for company, average in zip(companies, averages):
            print(F"{company:<8}: RM {average:.2f}")

    elif choice == 3:
        highest = np.max(prices)
        index = np.argmax(prices)
        row, column = np.unravel_index(index, prices.shape)
        print(f"Highest Stock Price : RM {highest:.2f}")
        print(f"Company : {companies[row]}")
        print(f"Day : {days[column]}")

    elif choice == 4:
        lowest = np.min(prices)
        index = np.argmin(prices)
        row, column = np.unravel_index(index, prices.shape)
        print(f"Lowest Stock Price : {lowest:.2f}")
        print(f"Company : {companies[row]}")
        print(f"Day : {days[column]}")

    elif choice == 5:
        percentage = float(input("Enter percentage: "))
        prices = prices * (1 + percentage / 100)
        print("Prices updated successfully!")
        
    elif choice == 6:
        for index, company in enumerate(companies, start=1):
            print (f"{index}. {company}")
        choice = int(input("Select the company :"))
        index = choice - 1
        print(companies[index])
        for day, price in zip(days, prices[index]):
            print(f"{day}: RM {price}")

    elif choice == 7:
        for index, day in enumerate(days, start=1):
            print (f"{index}. {day}")
        choice = int(input("Select the day :"))
        index = choice - 1
        print(f"\n{days[index]}\n")
        for company, price in zip(companies, prices[:, index]):
            print(f"{company}: RM {price}")
    else:
        print("Thank you for using Stock MaCrket Analyzer!")
        break