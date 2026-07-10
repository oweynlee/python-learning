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
           "Highest stock price","Lowest stock price",
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
        choice = int(input("Enter your choice: "))
    elif choice == 1:
        for index, company in enumerate(companies):
            print(f"\n{company} ")
            for day_index,day in enumerate(days):
                print(f"{day:<10}: RM{prices[index][day_index]}")

    elif choice == 2:
        print("Average Stock Price")
        averages = np.mean(prices, axis=1)
        for company, average in zip(companies, averages):
            print(F"{company:<8}: RM {average:.2f}")
    elif choice == 3:
        print("Feature coming soon...")
    elif choice == 4:
        pas
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    else:
        print("Thank you for using Stock Market Analyzer!")
        break
