import pandas as pd

df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva", "Bob", "Frank"],
    "Class": ["A", "B", "A", "B", "A", "B", "A"],
    "Math": [85, 92, 78, None, 95, 92, 88],
    "English": [90, 75, 91, 82, None, 75, 84]
})

df.drop_duplicates(inplace=True)    

df["Math"] = df["Math"].fillna(df["Math"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

print(df.round(2))

print(f"Math Average: {df['Math'].mean():.2f}, English Average: {df['English'].mean():.2f}")

print(df["Class"].value_counts())

print(df.groupby("Class")[["Math", "English"]].agg(["mean","max","min"]).sort_values(by=[("Math", "mean")], ascending=False))