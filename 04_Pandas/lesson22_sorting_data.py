import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Class": ["A", "B", "A", "B", "A"],
    "Score": [85, 92, 78, 88, 85]
})

print(df)

print(df.sort_values("Score"))  # According to ascendant order (smallest to largest)
print(df.sort_values("Score", ascending=False))     # Largest to smallest


print(df.sort_values(["Class", "Score"], ascending=[True, False]))

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"]
}, index=[2, 0, 1])

print(df)

print(df.sort_index()) # Sort index