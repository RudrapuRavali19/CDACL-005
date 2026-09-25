import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

print("Loading...")
df = pd.read_csv("purchase_pattern_analytics")

# Clean
df['Product'] = df['Product'].str.strip().str.lower()
df = df.drop_duplicates(subset=['TransactionID','Product'])

# Make baskets per bill
baskets = df.groupby('TransactionID')['Product'].apply(list).tolist()
print(f"Total Bills: {len(baskets)}")
print(f"Sample Bill: {baskets[0]}")

# Convert to 0/1 table
te = TransactionEncoder()
te_ary = te.fit(baskets).transform(baskets)
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# Apriori
print("Finding patterns...")
frequent = apriori(df_onehot, min_support=0.02, use_colnames=True)
rules = association_rules(frequent, metric="lift", min_threshold=1.2)
rules = rules.sort_values('lift', ascending=False)

# Save
frequent.to_csv("frequent_items.csv", index=False)
rules.to_csv("association_rules.csv", index=False)

print("\n--- TOP 5 RULES FOR YOUR PPT ---")
print(rules[['antecedents','consequents','support','confidence','lift']].head(10))
print("\nDONE! 2 new files created: frequent_items.csv, association_rules.csv")