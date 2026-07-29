import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

# Create a new column
df["Tax"] = df["Price"] * 0.10

print(df)