import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("purchase_pattern_analytics")

print("Making graphs...")

# Graph 1: Top 10 Products Bar Chart
top_products = df['Product'].value_counts().head(10)
plt.figure()
top_products.plot(kind='bar')
plt.title('Top 10 Selling Products')
plt.xlabel('Product')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graph1_top_products.png')
print("Saved graph1_top_products.png")

# Graph 2: Quantity Distribution (Histogram)
plt.figure()
df['Quantity'].hist(bins=10)
plt.title('Quantity Distribution')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.savefig('graph2_quantity.png')
print("Saved graph2_quantity.png")

# Graph 3: UnitPrice Distribution
plt.figure()
df['UnitPrice'].hist(bins=20)
plt.title('UnitPrice Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('graph3_price.png')
print("Saved graph3_price.png")

print("ALL 3 GRAPHS DONE! Check folder")