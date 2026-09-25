import pandas as pd
df = pd.read_csv("purchase_pattern_analytics")

print("--- EDA START ---")
print(f"\n1. Size: {df.shape[0]} rows, {df.shape[1]} columns")

print(f"\n2. Columns: {list(df.columns)}")

print(f"\n3. Missing values:\n{df.isnull().sum()}")


print(f"\n4. Unique Bills: {df['TransactionID'].nunique()}")
print(f" Unique Customers: {df['CustomerID'].nunique()}")
print(f" Unique Products: {df['Product'].nunique()}")

print(f"\n5. Top 10 Products Sold Most:\n{df['Product'].value_counts().head(10)}")

print(f"\n6. One Bill Example (T00001):\n{df[df['TransactionID']=='T00001'][['Product','Quantity']]}")

print("\n--- EDA DONE ---")