import pandas as pd

df = pd.DataFrame({
    "Salesperson": ["Alice", "Bob", "Alice", "David", "Bob", "Eva", "David", "Alice"],
    "Region": ["North", "South", "East", "North", "East", "South", "East", "North"],
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Laptop", "Phone", "Laptop", "Tablet"],
    "Sales": [2500, 1200, 2600, 1800, 2400, 1500, 2800, 1900]
})

print(df)

salesperson_ranking = (df.groupby("Salesperson")["Sales"]
      .sum()
      .sort_values(ascending=False)
      )

product_ranking = (df.groupby("Product")["Sales"]
      .sum()
      .sort_values(ascending=False)
      )

region_ranking = (df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
      )

print(
    "The highest sales were made by:",
    salesperson_ranking.index[0]
    )

print(f"Best-selling product: {product_ranking.index[0]}")
print(product_ranking)

print(f"Best-selling region: {region_ranking.index[0]}")
print(region_ranking)

salesperson_product_ranking = (df.groupby(["Salesperson", "Product"])["Sales"]
        .sum()
        .sort_values(ascending=False)
        )
print(f"Best-selling salesperson-product combination: {salesperson_product_ranking.index[0]}")
print(salesperson_product_ranking)

laptop_sales = (df[df["Product"] == "Laptop"]
        .groupby("Salesperson")["Sales"]
        .sum()
        .sort_values(ascending=False)
)
print(f"Laptop Sales by Salesperson: {laptop_sales.index[0]}")
print(laptop_sales)

laptop_sales_region = (df[df["Product"] == "Laptop"]
        .groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
)
print(f"Laptop Sales by Region: {laptop_sales_region.index[0]}")
print(laptop_sales_region)