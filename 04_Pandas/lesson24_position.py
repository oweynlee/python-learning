import pandas as pd

df = pd.DataFrame(
    {"Name": ["Alice", "Bob", "Charlie"]},
    index=[101, 102, 103]
)

df.loc[102]
df.iloc[1]
df.loc[1]