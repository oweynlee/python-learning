fruits = ["Apple", "Banana", "Orange"] # treat fruits as a bookshelf, and apple... are the books

print(fruits)   # list start at 0 
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits.append("Mango")  # Add a new value at the end of list
print(fruits)
fruits.remove("Banana") # Remove the value from the list
print(fruits)
fruits[0] = "Watermelon"    # Change the value at the specific position (Replace)
print(fruits)

#Lists are mutable, which means they can be modified after they're created.

print(len(fruits)) # Track the length of the list

# ----------------------------------- #

stocks = ["TSLA", "AAPL", "NVDA", "MSFT", "GOOGL"]

print(stocks)
print(len(stocks))
for stock in stocks:
    print(stock)