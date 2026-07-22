import pandas as pd

df = pd.DataFrame({
    "OrderID": [1001, 1002, 1002, 1003],
    "Customer": ["Alice", "Bob", "Bob", "Charlie"],
    "Amount": [120, 80, 80, 150]
})

print(df)
print(df.duplicated())  # False = Non-duplicated, True = Duplicated data By row
print(df.duplicated().sum())
print(df.drop_duplicates()) # Delete duplicated data, only left one at the first occurance

df = df.drop_duplicates().reset_index(drop=True)    # Reset the index back to, 0,1,2
print(df["Customer"].duplicated())      # Only check specific column