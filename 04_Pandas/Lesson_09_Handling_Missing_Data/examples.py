import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [22, None, 24, 21],
    "Salary": [4500, 5200, None, 4800]
})

print(df)
print(df.isna())    # ask "Is this value missing", NaN = True; Value = False
print(df.isna().sum()) #Count how many missing value
df.fillna(0)        # Replace NaN to 0

df.fillna(df.mean(numeric_only=True))       # Ignore the NaN and calculate the rest into mean and replace the mean to NaN
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())              # Replace as the mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df.dropna())                                          # Remove the entire row that contain NaN

print(df)