import pandas as pd

df = pd.read_csv("purchase_pattern_analytics")

print("--- KEY STATISTICS ---")

print("\n1. QUANTITY Stats:")
print(f" Mean (Average): {df['Quantity'].mean():.2f}")
print(f" Median (Middle): {df['Quantity'].median()}")
print(f" Mode (Most repeated): {df['Quantity'].mode()[0]}")
print(f" Min: {df['Quantity'].min()} Max: {df['Quantity'].max()}")

print("\n2. UNIT PRICE Stats:")
print(f" Mean (Average Price): {df['UnitPrice'].mean():.2f}")
print(f" Median: {df['UnitPrice'].median():.2f}")
print(f" Mode: {df['UnitPrice'].mode()[0]}")
print(f" Min: {df['UnitPrice'].min()} Max: {df['UnitPrice'].max()}")

df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
print("\n3. TOTAL AMOUNT (Quantity*Price) Stats:")
print(f" Mean: {df['TotalAmount'].mean():.2f}")
print(f" Median: {df['TotalAmount'].median():.2f}")
print(f" Highest Bill Item: {df['TotalAmount'].max():.2f}")

print(f"\n4. Std Dev - Quantity: {df['Quantity'].std():.2f}")
print(f" Std Dev - Price: {df['UnitPrice'].std():.2f}")

print("\n--- STATS DONE ---")