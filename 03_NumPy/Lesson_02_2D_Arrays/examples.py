import numpy as np

scores = np.array([
    [85, 90, 88],   # Row 0
    [78, 82, 80],   # Row 1
    [92, 95, 91]    # Row 2
])

print(scores[1])    # Print Full Row
print(scores[0,1])  # Print (Row, Collumn)
print(scores[0,:])  # Collon (:) beside everything but the row
print(scores[:, 0]) # beside everthing but the collumn

mark = np.array([85, 90, 88, 92, 95])

print(np.mean(mark))   # Average

print(np.sum(mark))    # Total

print(np.max(mark))    # Highest value

print(np.min(mark))    # Lowest value

prices = np.array([
    [180, 182, 185],
    [240, 238, 245],
    [980, 995, 1010]
])

print(prices * (1 + 5/100))