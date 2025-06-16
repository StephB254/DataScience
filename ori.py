import pandas as pd, numpy as np, matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_excel('Online Retail.xlsx', sheet_name='Online Retail', nrows=5000)
output_dir = Path("analysis_outputs"); output_dir.mkdir(exist_ok=True)

df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['CustomerID'] = df['CustomerID'].fillna(-1)
df = df.dropna(subset=['Description'])
valid_df = df[df['Revenue'] > 0]

def summary_stats(s): return {
    "mean": round(s.mean(), 2), "median": round(s.median(), 2),
    "mode": s.mode().iloc[0] if not s.mode().empty else None,
    "std_dev": round(s.std(ddof=1), 2),
    "min": round(s.min(), 2), "max": round(s.max(), 2),
    "range": round(s.max() - s.min(), 2)
}

stats_report = {
    "Quantity Stats": summary_stats(valid_df['Quantity']),
    "Unit Price Stats": summary_stats(valid_df['UnitPrice']),
    "Revenue Stats": summary_stats(valid_df['Revenue']),
    "Most Common Country": df['Country'].mode().iloc[0],
    "Return Rate (%)": round((df['Revenue'] < 0).mean() * 100, 2)
}

with open(output_dir / "stats.txt", "w") as f:
    for k, v in stats_report.items(): f.write(f"{k}:\n{v}\n\n")

plt.rcParams.update({
    'figure.figsize': (10, 6), 'axes.titlesize': 14, 'axes.labelsize': 12,
    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'axes.titleweight': 'bold', 'axes.grid': True
})

def save_plot(title, xlabel, ylabel, filename):
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel)
    plt.tight_layout(); plt.savefig(output_dir / f"{filename}.png", dpi=300); plt.close()

plt.hist(valid_df['Quantity'], bins=50, color='skyblue', edgecolor='black')
save_plot("Histogram-Quanntity", "Quantity", "Frequency", "quantity_hist")

plt.hist(valid_df['UnitPrice'], bins=50, color='orange', edgecolor='black')
save_plot("Histogram-Unit Price", "Unit Price", "Frequency", "unitprice_hist")

daily_revenue = valid_df.set_index('InvoiceDate').resample('D')['Revenue'].sum()
plt.plot(daily_revenue.index, daily_revenue.values, color='green', marker='o', linestyle='-')
save_plot("Daily Revenue Trend", "Date", "Revenue", "daily_revenue")

top_customers = valid_df.groupby('CustomerID')['Revenue'].sum().nlargest(10)
plt.bar(top_customers.index.astype(str), top_customers.values, color='steelblue')
save_plot("Top 10 Customers-Revenue", "Customer ID", "Total Revenue", "top_customers")

top_countries = valid_df.groupby('Country')['Revenue'].sum().nlargest(10)
plt.bar(top_countries.index, top_countries.values, color='darkgreen')
save_plot("Top 10 Countries-Revenue", "Country", "Total Revenue", "top_countries")
