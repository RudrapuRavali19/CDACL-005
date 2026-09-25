import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

print("=== CDACL-005 Enhanced Iteration 2.0 ===")

basket = pd.read_csv("basket_for_apriori.csv", index_col=0)
print(f"Loaded Basket: {basket.shape}") 
frequent_items = apriori(basket, min_support=0.02, use_colnames=True)
print(f"Iteration 1 - Frequent Itemsets: {len(frequent_items)}")

frequent_items['length'] = frequent_items['itemsets'].apply(lambda x: len(x))
frequent_items = frequent_items[frequent_items['length'] <= 3] # Remove too big combos
print(f"After Length Filter: {len(frequent_items)} itemsets")

frequent_items['itemsets_str'] = frequent_items['itemsets'].apply(lambda x: ', '.join(list(x)))
frequent_items[['support','itemsets_str','length']].to_csv("frequent_items_enhanced.csv", index=False)

rules = association_rules(frequent_items, metric="confidence", min_threshold=0.3)
rules = rules.sort_values(by='lift', ascending=False)

high_quality_rules = rules[(rules['lift'] > 1.5) & (rules['confidence'] > 0.5)]
print(f"Total Rules: {len(rules)} | High-Quality Rules: {len(high_quality_rules)}")

rules['profit_score'] = rules['support'] * rules['confidence'] * rules['lift']
rules = rules.sort_values(by='profit_score', ascending=False)

rules['antecedents_str'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents_str'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
rules[['antecedents_str','consequents_str','support','confidence','lift','profit_score']].to_csv("association_rules_enhanced.csv", index=False)

print("\n=== TOP 5 MOST PROFITABLE RULES (New Metric) ===")
print(rules[['antecedents_str','consequents_str','confidence','lift','profit_score']].head(5).to_string())

print(f"\nDONE - {len(rules)} Total Rules, {len(high_quality_rules)} High-Quality Rules - Enhanced Iteration Complete!")