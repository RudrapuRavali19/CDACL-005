import pandas as pd
import matplotlib.pyplot as plt

rules = pd.read_csv("association_rules.csv")
print("Columns:", rules.columns.tolist())
print(f"Loaded {len(rules)} rules")

ant_col = 'antecedents' if 'antecedents' in rules.columns else 'antecedents_str'
cons_col = 'consequents' if 'consequents' in rules.columns else 'consequents_str'

top10_lift = rules.sort_values(by='lift', ascending=False).head(10)
plt.figure(figsize=(12,6))
labels = top10_lift[ant_col].astype(str) + " -> " + top10_lift[cons_col].astype(str)
plt.barh(labels, top10_lift['lift'], color='darkorange')
plt.xlabel("Lift")
plt.title("Graph 6: Top 10 Association Rules by Lift (Strongest)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("graph6_top_rules_lift.png")
print("Graph6 saved!")

top10_conf = rules.sort_values(by='confidence', ascending=False).head(10)
plt.figure(figsize=(12,6))
labels2 = top10_conf[ant_col].astype(str) + " -> " + top10_conf[cons_col].astype(str)
plt.barh(labels2, top10_conf['confidence'], color='seagreen')
plt.xlabel("Confidence")
plt.title("Graph 7: Top 10 Rules by Confidence")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("graph7_top_rules_confidence.png")
print("Graph7 saved!")

plt.figure(figsize=(10,6))
plt.scatter(rules['support'], rules['confidence'], c=rules['lift'], cmap='viridis', alpha=0.6)
plt.colorbar(label='Lift')
plt.xlabel("Support")
plt.ylabel("Confidence")
plt.title("Graph 8: Support vs Confidence (Color=Lift)")
plt.tight_layout()
plt.savefig("graph8_support_confidence_lift.png")
print("Graph8 saved!")
frequent = pd.read_csv("frequent_items.csv")
print("Frequent Columns:", frequent.columns.tolist())
item_col = 'itemsets' if 'itemsets' in frequent.columns else 'itemsets_str'
top15 = frequent.sort_values(by='support', ascending=False).head(15)
plt.figure(figsize=(12,6))
plt.barh(top15[item_col].astype(str), top15['support'], color='skyblue')
plt.xlabel("Support")
plt.title("Graph 9: Top 15 Frequent Itemsets")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("graph9_frequent_itemsets.png")
print("Graph9 saved!")

print("\nALL APRIORI GRAPHS DONE!")