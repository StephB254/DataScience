# Full implementation of p1_code_challenge.ipynb with compliance to instructions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numbers import Number

# Step 1.1: Load dataset
df = pd.read_csv("/mnt/data/fifa.csv")

# Step 1.2: Convert 'Release Clause' from Euro to Dollar (1 Euro = 1.2 Dollars)
df['Release Clause'] = df['Release Clause'].replace('€', '', regex=True).replace('M', 'e6', regex=True).replace('K', 'e3', regex=True)
df['Release Clause'] = pd.to_numeric(df['Release Clause'], errors='coerce') * 1.2

# Step 1.3: Drop rows with missing 'Release Clause'
df = df.dropna(subset=['Release Clause'])

# Step 1.4: Top 10 countries by player count
top_10_countries = df['Nationality'].value_counts().head(10).index.tolist()

# Step 2.1: Bar chart for 5 specific countries
bar_chart_countries = ['England', 'Germany', 'Spain', 'France', 'Argentina']
bar_chart_title = '5 Countries with the Most Players'
bar_chart_xlabel = 'Country'
bar_chart_ylabel = 'Number of Players'

player_counts = df['Nationality'].value_counts().loc[bar_chart_countries]
player_count_figure, ax1 = plt.subplots()
ax1.bar(player_counts.index, player_counts.values)
ax1.set_title(bar_chart_title)
ax1.set_xlabel(bar_chart_xlabel)
ax1.set_ylabel(bar_chart_ylabel)
plt.tight_layout()

# Step 2.2: Scatter plot - Standing vs Sliding Tackle
scatter_plot_title = 'Relationship Between Standing Tackles and Sliding Tackles'
standing_tackle_label = 'Standing Tackles'
sliding_tackle_label = 'Sliding Tackles'

tackle_figure, ax2 = plt.subplots()
ax2.scatter(df['StandingTackle'], df['SlidingTackle'], alpha=0.5)
ax2.set_title(scatter_plot_title)
ax2.set_xlabel(standing_tackle_label)
ax2.set_ylabel(sliding_tackle_label)
plt.tight_layout()

# Step 3.1: Mean and Median Age
mean_age = df['Age'].mean()
median_age = df['Age'].median()

# Step 3.2: Oldest Argentine Player
argentines = df[df['Nationality'] == 'Argentina']
oldest_argentine = argentines.loc[argentines['Age'].idxmax()]
oldest_argentine_name = oldest_argentine['Name']
oldest_argentine_age = oldest_argentine['Age']

# Step 4.1: List of player names from dictionary
players = {
    'L. Messi': {'age': 31, 'nationality': 'Argentina', 'teams': ['Barcelona']},
    'Cristiano Ronaldo': {'age': 33, 'nationality': 'Portugal', 'teams': ['Juventus', 'Manchester United']},
    'Neymar': {'age': 26, 'nationality': 'Brazil', 'teams': ['PSG']},
    'De Gea': {'age': 27, 'nationality': 'Spain', 'teams': ['Manchester United']}
}
player_names = list(players.keys())

# Step 4.2: List of tuples (name, nationality)
player_nationalities = [(name, info['nationality']) for name, info in players.items()]

# Step 4.3: Function to get players on a specific team
def get_players_on_team(player_dict, team_name):
    return [name for name, info in player_dict.items() if team_name in info['teams']]
