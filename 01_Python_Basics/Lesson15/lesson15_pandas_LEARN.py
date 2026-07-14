import pandas as pd

data = {
    "Company": ["Apple", "Tesla", "Nvidia"],
    "Price": [180, 240, 980],
    "Country": ["USA", "USA", "USA"]
}

df = pd.DataFrame(data)
print(df)

print(df.head())    # Print first 5 row of the list
print(df.columns)   # Index(['Company', 'Price', 'Country'], dtype='object')
print(df.shape)     # Print the size of the DataFrame (row, column)


scores = [80, 90, 100]
scores[0] = 95  # [] list can be modified
shape = (5,3)   # inside () is a tuple, which can be modified. // df.shape
#Read-only information

BASE_DIR = Path(__file__).parent

csv_path = BASE_DIR / "stocks.csv"

# Different from the one line expenses tracker, as we have many csv, thus we can use BASE_DIR repeatedly
