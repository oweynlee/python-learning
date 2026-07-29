import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

print(df)

print("\nPrice > 200")
print(df[df["Price"] > 200])

print("\nPrice > 200 AND Country == USA")
print(df[(df["Price"] > 200) & (df["Country"] == "USA")])   # AND statement

print("\nPrice > 200 OR Country == Korea")
print(df[(df["Price"] > 200) | (df["Country"] == "Korea")]) # OR statement

print("\nNOT USA")
print(df[~(df["Country"] == "USA")])                        # NOT statement

