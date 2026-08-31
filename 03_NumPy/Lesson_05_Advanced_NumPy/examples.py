import numpy as np

scores = np.array([55, 70, 85, 90, 65])

scores[scores > 20]
scores[(scores > 30) & (scores < 90)]   # (AND) Two condition must be true to be true, else is false
scores[(scores > 30) | (scores < 90)]   # (OR) One condition must be true to be true
scores[~(scores > 20)]                  # (NOT) Opposite of the statement


result = np.where(scores >= 70, "Pass", "Fail")
#   np.where(condition, value_if_true, value_if_false)

print(result)

