import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Step 1: Import pandas (already done)

# Step 2: Load the dataset
housing_data = pd.read_csv("ames_housing.csv")

# Step 3: Create a new column 'price_per_square_ft'
housing_data["price_per_square_ft"] = housing_data["SalePrice"] / housing_data["GrLivArea"]

# Step 4: Calculate the mean of price_per_square_ft
mean_price_per_square_ft = housing_data["price_per_square_ft"].mean()

# Step 5: Plot average price per square foot for selected neighborhoods
selected_neighborhoods = ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst"]
subset = housing_data[housing_data["Neighborhood"].isin(selected_neighborhoods)]

x = "Neighborhood"
y = "price_per_square_ft"

avg_prices = subset.groupby(x)[y].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_prices.plot(kind="bar")
plt.title("Average Price per Square Foot by Neighborhood")
plt.ylabel("Price per Square Foot")
plt.xlabel("Neighborhood")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Identify the most common neighborhood
name = housing_data["Neighborhood"].mode()[0]
frequency = housing_data["Neighborhood"].value_counts().loc[name]
