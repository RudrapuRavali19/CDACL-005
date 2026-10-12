import pandas as pd
import matplotlib.pyplot as plt

rules = pd.read_csv("association_rules.csv")
print("Loaded", len(rules), "rules")

# Graph 6 - PERFECT - All Lift 13.9x so show Confidence also
plt.figure(figsize=(13,8), dpi=300)
top6 = rules.nlargest(10, 'lift')
labels6 = [f"{str(a)[:22]}->{str(c)[:12]}" for a,c in zip(top6['antecedents_str'], top6['consequents_str'])]

bars = plt.barh(labels6[::-1], top6['lift'][::-1], color='#1976d2', edgecolor='white', linewidth=1)
plt.title('Graph 6: Top 10 Rules by Lift (13.9x Stronger)', fontsize=14, fontweight='bold', color='#0d47a1', pad=15)
plt.xlabel('Lift Value (Times more likely than random)', fontsize=12, fontweight='bold')
plt.grid(axis='x', alpha=0.3, linestyle='--')

# Show values on bars - THIS FIXES SAME BAR ISSUE
for bar, conf, lift, supp in zip(bars, top6['confidence'][::-1], top6['lift'][::-1], top6['support'][::-1]):
    plt.text(bar.get_width()+0.2, bar.get_y()+bar.get_height()/2, f'Lift: {lift:.1f}x | Conf: {conf:.0%} | Sup: {supp:.3f}', va='center', fontweight='bold', fontsize=9)

plt.text(0.02, 0.98, "All Top Rules have 13.9x Lift\n-> 14 times more likely to buy together!\n-> Best for combo offers", transform=plt.gca().transAxes, va='top', ha='left',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#e3f2fd", edgecolor="#0d47a1"), fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('graph6_top_rules_lift_PERFECT.png', dpi=300, bbox_inches='tight')
print("Graph6 PERFECT saved!")

# Graph 7 - PERFECT - Shows WHY all same
plt.figure(figsize=(12,8), dpi=300)
top7 = rules.nlargest(10, 'lift')  # Use lift because confidence all 1.0
labels7 = [f"{str(a)[:22]}->{str(c)[:12]}" for a,c in zip(top7['antecedents_str'], top7['consequents_str'])]

# Two colors - Confidence (pink) + Lift text
bars = plt.barh(labels7[::-1], top7['lift'][::-1], color='#e91e63', edgecolor='white', linewidth=1)
plt.title('Graph 7: Top 10 Rules - 100% Confidence + High Lift', fontsize=14, fontweight='bold', color='#880e4f', pad=15)
plt.xlabel('Lift Value (Times more likely)', fontsize=12, fontweight='bold')
plt.grid(axis='x', alpha=0.3, linestyle='--')

# Show Confidence and Lift values on bars
for bar, conf, lift in zip(bars, top7['confidence'][::-1], top7['lift'][::-1]):
    plt.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2, f'Conf: {conf:.0%} | Lift: {lift:.1f}x', va='center', fontweight='bold', fontsize=9)

plt.text(0.02, 0.98, "All rules have 100% Confidence\n-> Perfect for combo offers!", transform=plt.gca().transAxes, va='top', ha='left',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#fce4ec", edgecolor="#880e4f"), fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('graph7_top_rules_confidence_PERFECT.png', dpi=300, bbox_inches='tight')
print("Graph7 PERFECT saved!")

# Graph 8
# Graph 8 - PERFECT - Support vs Confidence
plt.figure(figsize=(11,7), dpi=300)
scatter = plt.scatter(rules['support'], rules['confidence'], 
                      c=rules['lift'], cmap='viridis', 
                      alpha=0.8, s=90, edgecolor='white', linewidth=0.8)

cbar = plt.colorbar(scatter)
cbar.set_label('Lift Value (Strength) - Yellow = Strongest', fontweight='bold', fontsize=11)

plt.title('Graph 8: Support vs Confidence (Color = Lift) - 703 Rules', fontsize=14, fontweight='bold', color='#0d47a1', pad=15)
plt.xlabel('Support (How frequent is rule)', fontsize=12, fontweight='bold')
plt.ylabel('Confidence (How reliable)', fontsize=12, fontweight='bold')
plt.grid(alpha=0.3, linestyle='--')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Insight box - THIS MAKES IT PERFECT FOR REPORT
plt.text(0.65, 0.25, 
         "Insight:\n• Top cluster: Support ~0.07, Confidence ~0.95\n• High Confidence (1.0) = Perfect combo\n• Yellow dots = 13.9x Lift (Best offers)\n• Low Support + High Conf = Niche but strong",
         transform=plt.gca().transAxes, va='center', ha='left',
         bbox=dict(boxstyle="round,pad=0.6", facecolor="#fff9c4", edgecolor="#f57f17", alpha=0.9),
         fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('graph8_support_confidence_PERFECT.png', dpi=300, bbox_inches='tight')
print("Graph8 PERFECT saved!")

# Graph 9 - PERFECT - Top 15 Frequent Itemsets - REAL
import pandas as pd
try:
    # Try to load frequent itemsets if you have file
    freq = pd.read_csv("frequent_itemsets.csv")
    # Check column name
    if 'itemsets' in freq.columns:
        col = 'itemsets'
    elif 'itemsets_str' in freq.columns:
        col = 'itemsets_str'
    else:
        col = freq.columns[0]

    top9 = freq.nlargest(15, 'support')
    labels9 = [str(x)[:30] for x in top9[col]]
    supports9 = top9['support']

    plt.figure(figsize=(14,8), dpi=300)
    bars = plt.barh(labels9[::-1], supports9[::-1], color='#2e7d32', edgecolor='white', linewidth=1)
    plt.title('Graph 9: Top 15 Frequent Itemsets (Most Bought Together)', fontsize=14, fontweight='bold', color='#1b5e20', pad=15)
    plt.xlabel('Support (Frequency of buying together)', fontsize=12, fontweight='bold')
    plt.grid(axis='x', alpha=0.3, linestyle='--')

    for bar, sup in zip(bars, supports9[::-1]):
        plt.text(bar.get_width()+0.002, bar.get_y()+bar.get_height()/2, f'{sup:.3f}', va='center', fontweight='bold', fontsize=9)

    plt.text(0.02, 0.98, "Insight:\n• Highest support = Most frequent combo\n• Stock these together\n• Place at eye level",
             transform=plt.gca().transAxes, va='top', ha='left',
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#e8f5e9", edgecolor="#1b5e20"), fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.savefig('graph9_frequent_itemsets_PERFECT.png', dpi=300, bbox_inches='tight')
    print("Graph9 PERFECT saved!")

except:
    # If no frequent_itemsets.csv, make from rules
    plt.figure(figsize=(14,8), dpi=300)
    # Count individual items from rules
    from collections import Counter
    all_items = []
    for a in rules['antecedents_str']:
        all_items.extend([x.strip() for x in str(a).split(',')])
    for c in rules['consequents_str']:
        all_items.extend([x.strip() for x in str(c).split(',')])

    counter = Counter(all_items)
    top_items = counter.most_common(15)
    labels9 = [x[0][:25] for x in top_items]
    counts9 = [x[1] for x in top_items]

    bars = plt.barh(labels9[::-1], counts9[::-1], color='#2e7d32', edgecolor='white')
    plt.title('Graph 9: Top 15 Most Frequent Products', fontsize=14, fontweight='bold', color='#1b5e20', pad=15)
    plt.xlabel('Frequency in Rules (Popularity)', fontsize=12, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('graph9_frequent_itemsets_PERFECT.png', dpi=300, bbox_inches='tight')
    print("Graph9 PERFECT saved! (from rules)")