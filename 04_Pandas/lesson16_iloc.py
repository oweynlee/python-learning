import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

print(df)

print("\n----- iloc Examples -----")

# First row
print(df.iloc[0])

# Second row
print(df.iloc[1])

# Third row
print(df.iloc[2])

print("\n----- Specific Values -----")

# First row, Company column
print(df.iloc[0, 0])

# Second row, Price column
print(df.iloc[1, 1])

# Third row, Country column
print(df.iloc[2, 2])