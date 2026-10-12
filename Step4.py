import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("purchase_pattern_analytics.csv")

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

# Graph 2 - PERFECT VERSION
plt.figure(figsize=(11,7), dpi=300)

# Check quantity distribution
qty_counts = df['Quantity'].value_counts().sort_index()

bars = plt.bar(qty_counts.index.astype(str), qty_counts.values, 
               color=['#ff9800','#ffb74d','#ff9800','#f57c00','#ef6c00'], 
               edgecolor='black', linewidth=0.8, width=0.6)

plt.title('Graph 2: Quantity Distribution - Customer Buying Pattern', 
          fontsize=14, fontweight='bold', color='#e65100', pad=15)
plt.xlabel('Quantity Purchased (Units)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency (Number of Transactions)', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Add values on top
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()+500, 
             f'{int(bar.get_height()):,}', ha='center', va='bottom', 
             fontweight='bold', fontsize=11)

plt.text(0.02, 0.95, 
         f"Insight:\n• Total Transactions: {len(df):,}\n• Avg Quantity: {df['Quantity'].mean():.1f}\n• Most common: {qty_counts.idxmax()} units\n• Uniform pattern = Bulk buying common",
         transform=plt.gca().transAxes, va='top', ha='left',
         bbox=dict(boxstyle="round,pad=0.6", facecolor="#fff3e0", edgecolor="#e65100", alpha=0.9),
         fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('graph2_quantity_PERFECT.png', dpi=300, bbox_inches='tight')
print("Graph2 PERFECT saved!")

# Graph 3 - PERFECT - Unit Price Distribution
plt.figure(figsize=(11,7), dpi=300)

# Use 20 bins to show distribution better
plt.hist(df['UnitPrice'], bins=20, color='#0288d1', edgecolor='white', linewidth=1, alpha=0.9)

plt.title('Graph 3: Unit Price Distribution - Pricing Strategy Insight', 
          fontsize=14, fontweight='bold', color='#01579b', pad=15)
plt.xlabel('Unit Price (₹)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency (Number of Products)', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')

plt.text(0.70, 0.85, 
         f"Insight:\n• Price Range: ₹{df['UnitPrice'].min():.0f} - ₹{df['UnitPrice'].max():.0f}\n• Avg Price: ₹{df['UnitPrice'].mean():.0f}\n• Most products under ₹400\n• Uniform = Diverse product range",
         transform=plt.gca().transAxes, va='top', ha='left',
         bbox=dict(boxstyle="round,pad=0.6", facecolor="#e1f5fe", edgecolor="#01579b", alpha=0.9),
         fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('graph3_price_PERFECT.png', dpi=300, bbox_inches='tight')
print("Graph3 PERFECT saved!")

