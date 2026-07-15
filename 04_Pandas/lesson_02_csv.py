# 14 July 2026
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"
# Different from the one line expenses tracker, as we have many csv, thus we can use BASE_DIR repeatedly

df = pd.read_csv(csv_path)

print(df.head())    # Print first 5 row of the list
print(df.columns)   # Index(['Company', 'Price', 'Country'], dtype='object')
print(df.shape)     # Print the size of the DataFrame (row, column)

print(df["Company"])
print(df[df["Price"] > 200])



scores = [80, 90, 100]
scores[0] = 95  # [] list can be modified
shape = (5,3)   # inside () is a tuple, which can be modified. // df.shape
#Read-only information
