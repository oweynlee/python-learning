import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Class": ["A", "B", "A", "B", "A"],
    "Score": [85, 92, 78, 88, 95]
})

print(df)

print(df["Score"]>85)   # Check the condition true or false
print(df[df["Score"] > 85]) # Print the true condition row

df[(df["Class"] == "B") | (df["Score"] >= 90)]

# Review same concept
