import pandas as pd

data = {
    "Company": ["Apple", "Tesla", "Nvidia"],
    "Price": [180, 240, 980],
    "Country": ["USA", "USA", "USA"]
}

df = pd.DataFrame(data)

print(df)