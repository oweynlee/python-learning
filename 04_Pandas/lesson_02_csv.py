from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

print(df.head())
print(df.columns)
print(df.shape)
print(df["Company"])
print(df[df["Price"] > 200])