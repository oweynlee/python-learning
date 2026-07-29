import pandas as pd

students = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

scores = pd.DataFrame({
    "StudentID": [2, 3, 5],
    "Math": [88, 91, 100]
})

print(students)
print()
print(scores)

result = pd.merge(students, scores, on="StudentID")     # Merge value of "StudentID", only matched value will be printed

print(result)

pd.merge(students, scores, on="StudentID", how="left") 

# inner	Only matching rows

# left	All rows from the left DataFrame

# right	All rows from the right DataFrame

# outer	All rows from both DataFrames