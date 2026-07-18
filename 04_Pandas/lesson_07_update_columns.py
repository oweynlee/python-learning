import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

print("Original:")
print(df)

# Increase every price by 10%
df["Price"] = df["Price"] * 1.10

print("\nAfter 10% Increase:")
print(df)