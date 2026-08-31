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

lowest = np.min(prices)
index = np.argmin(prices)
#   argmin is tell the python/user the exact index 
row, column = np.unravel_index(index, prices.shape)     
#   unravel_index means to tell the user exact location instead of just number, translate the index // len(element) per row . index % len(element) -> row, column
print(f"Lowest Stock Price : {lowest:.2f}")
print(f"Company : {companies[row]}")
print(f"Day : {days[column]}")