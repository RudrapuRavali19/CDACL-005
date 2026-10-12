import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('purchase_pattern_analytics_39k.csv')

plt.figure(figsize=(10,6))
quantity_counts = df['Quantity'].value_counts().sort_index()

plt.bar(quantity_counts.index.astype(str), quantity_counts.values, color='#FF9800', edgecolor='black', width=0.6)

plt.title('Graph 2: Quantity Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(quantity_counts.values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('graph2_quantity.png', dpi=300, bbox_inches='tight')
plt.close()

print("Graph2 FIXED - Generated graph2_quantity.png")
print(quantity_counts)