import pandas as pd
import numpy as np

# Load and clean dataset
df = pd.read_csv("heroes_information.csv", index_col=0)
df.replace("-", np.nan, inplace=True)

# Step 1: Filter to relevant columns
relevant_columns = ["name", "Eye color", "Alignment"]
df = df[relevant_columns]

# Step 2: Filter to rows where Alignment is 'good'
df = df[df["Alignment"] == "good"]

# Step 3: Drop rows with missing 'Eye color'
df = df.dropna(subset=["Eye color"])

# Step 4: Top 5 most common eye colors
top_eye_colors_series = df["Eye color"].value_counts().head(5)
top_eye_colors = top_eye_colors_series.index.tolist()
top_eye_color_counts = top_eye_colors_series.values.tolist()

# Step 5: Plot using pandas only
bar_chart_title = "Top 5 Most Common Superhero Eye Colors"
top_eye_colors_series.plot(kind="bar", title=bar_chart_title, xlabel="Eye Color", ylabel="Number of Superheroes", grid=True, figsize=(8, 5))
