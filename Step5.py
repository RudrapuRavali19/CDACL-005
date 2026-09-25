import pandas as pd

df = pd.read_csv("purchase_pattern_analytics")

print("--- OUTLIER & MISSING CHECK ---")

print("\n1. MISSING VALUES:")
print(df.isnull().sum())
print(f"Total missing: {df.isnull().sum().sum()}")

print(f"\n2. Duplicate rows: {df.duplicated().sum()}")

Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
outliers_qty = df[(df['Quantity'] < lower) | (df['Quantity'] > upper)]
print(f"\n3. Quantity Outlier Check:")
print(f" Q1={Q1}, Q3={Q3}, IQR={IQR}")
print(f" Normal range: {lower} to {upper}")
print(f" Outliers found: {len(outliers_qty)} rows")

Q1_p = df['UnitPrice'].quantile(0.25)
Q3_p = df['UnitPrice'].quantile(0.75)
IQR_p = Q3_p - Q1_p
lower_p = Q1_p - 1.5*IQR_p
upper_p = Q3_p + 1.5*IQR_p
outliers_price = df[(df['UnitPrice'] < lower_p) | (df['UnitPrice'] > upper_p)]
print(f"\n4. UnitPrice Outlier Check:")
print(f" Q1={Q1_p:.2f}, Q3={Q3_p:.2f}, IQR={IQR_p:.2f}")
print(f" Normal range: {lower_p:.2f} to {upper_p:.2f}")
print(f" Outliers found: {len(outliers_price)} rows")

if df.isnull().sum().sum() == 0:
    print("\n5. No missing values - No cleaning needed!")
else:
    print("\n5. Missing found - we will fill/remove")

print("\n--- CHECK DONE ---")