import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "stocks.csv"

df = pd.read_csv(csv_path)

print(df)

print(df.groupby("Country").size())     #.groupby() get the same "Country" as a group, .size() show how many in the group

print(df.groupby("Country")["Price"].mean())    # calculate the mean price per group
print(df.groupby("Country")["Price"].sum())    # calculate the sum price per group
print(df.groupby("Country")["Price"].min())    # find the smallest price per group
print(df.groupby("Country")["Price"].max())    # find the largest price per group
print(df.groupby("Country")["Price"].count())    # same as .size()
# .size() counts rows.
# .count() counts non-empty values in a specific column.

print(
    df.groupby("Country")["Price"].agg(["count", "sum", "mean", "min", "max"])  # Multiple Aggregations (Product multiple function in a go)
)