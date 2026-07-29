import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Class": ["A", "B", "A", "B", "A"],
    "Score": [85, 92, 78, 88, 95]
})

print(df)

print(df["Score"]>85)