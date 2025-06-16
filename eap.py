import pandas as pd, numpy as np, matplotlib.pyplot as plt
from pathlib import Path

df_raw = pd.read_excel('Online Retail.xlsx', sheet_name='Online Retail', nrows=5000)
df_raw['Revenue'] = df_raw['Quantity'] * df_raw['UnitPrice']
df_raw['CustomerID'].fillna(-1, inplace=True)
df_raw.dropna(subset=['Description'], inplace=True)
df_raw['Description'] = df_raw['Description'].str.strip()
df_raw['InvoiceDate'] = pd.to_datetime(df_raw['InvoiceDate'])

anomalies = df_raw[(df_raw['Revenue'] <= 0) | (df_raw['UnitPrice'] <= 0)].copy()
df = df_raw[(df_raw['Revenue'] > 0) & (df_raw['UnitPrice'] > 0) & (df_raw['Description'] != '')]
df = df[df['InvoiceNo'].astype(str).str.isnumeric()]

for col in ['Quantity', 'UnitPrice']:
    Q1, Q3 = df[col].quantile([.25, .75])
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

out = Path("enhanced_analysis"); out.mkdir(exist_ok=True)
def savefig(name): plt.tight_layout(); plt.savefig(out / f"{name}.png", dpi=300); plt.close()

top_qty = df.groupby('Description')['Quantity'].sum().nlargest(10)
top_rev = df.groupby('Description')['Revenue'].sum().nlargest(10)
returns = anomalies[anomalies['Revenue'] < 0].groupby('Description')['Quantity'].sum().nlargest(10)
avg_basket = df.groupby('InvoiceNo')['Quantity'].sum().mean()
df['Hour'] = df['InvoiceDate'].dt.hour
hr_rev = df.groupby('Hour')['Revenue'].sum()

plt.bar(top_qty.index, top_qty.values); plt.xticks(rotation=45); plt.title("Top Products-Quantity"); plt.xlabel("Product"); plt.ylabel("Total Sold"); savefig("leading_by_quantitty")
plt.bar(top_rev.index, top_rev.values); plt.xticks(rotation=45); plt.title("Top Products-Revenue"); plt.xlabel("Product"); plt.ylabel("Total Revenue"); savefig("leading_by_revenue")
if not returns.empty: plt.bar(returns.index, returns.values); plt.xticks(rotation=45); plt.title("Most Returned Products"); plt.xlabel("Product"); plt.ylabel("Returned Qty"); savefig("most_returened_product")
plt.bar(hr_rev.index, hr_rev.values); plt.title("Revenue-Hour"); plt.xlabel("Hour of Day"); plt.ylabel("Revenue"); savefig("hourly_revenue")

with open(out / "enhanced_analysis.txt", "w") as f:
    f.write(f"Average Basket Size: {avg_basket:.2f}\n\n")
    f.write("Top 10 Products-Quantity:\n" + top_qty.to_string() + "\n\n")
    f.write("Top 10 Products-Revenue:\n" + top_rev.to_string() + "\n\n")
    f.write("Most Returned Procdut:\n" + (returns.to_string() if not returns.empty else "None detected.") + "\n")
