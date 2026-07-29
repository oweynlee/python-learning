# 15 July 2026
import pandas as pd

data = {
    "Company": ["Apple", "Tesla", "Nvidia"],
    "Price": [180, 240, 980],
    "Country": ["USA", "USA", "USA"]
}

df = pd.DataFrame(data)

print(df.info())                                        # Show info, dtype
print(df.describe("Price"))                             # Show mean, min, max, count
print(df.sort_values("Price", ascending=False))         # Sort from smallest to largest(ascending=True), largest to smallest (ascending=False)
print(df.loc[row, column])                              # Show a selected specific value