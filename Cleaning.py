import pandas as pd
df = pd.read_csv("purchase_pattern_analytics")
print("Initial Shape:", df.shape)
print("--- MISSING VALUES ---")
print(df.isnull().sum())
print("Total Missing %:", df.isnull().sum().sum() / len(df) * 100)

print("--- DUPLICATES ---")
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates() 
print("--- BEFORE CLEANING ---")
print(df['Product'].unique())


df['Product'] = df['Product'].str.strip()  
df['Product'] = df['Product'].str.title()  

print("--- AFTER CLEANING ---")
print(df['Product'].unique())
print("Total Products:", df['Product'].nunique())
print("--- DATE ---")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print(df['Date'].head())
print("Any invalid dates:", df['Date'].isnull().sum())
print("--- NEGATIVE CHECK ---")
print("Quantity <=0:", (df['Quantity'] <= 0).sum())
print("UnitPrice <=0:", (df['UnitPrice'] <= 0).sum())
print("--- OUTLIERS - QUANTITY ---")
Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
print(f"Q1={Q1}, Q3={Q3}, IQR={IQR}")
print(f"Allowed Range: {lower} to {upper}")
print(f"Min={df['Quantity'].min()}, Max={df['Quantity'].max()}")
print("--- OUTLIERS - PRICE ---")
print(df['UnitPrice'].describe())
print("--- FINAL ---")
print("Final Shape:", df.shape)
print(df.isnull().sum())
df.to_csv("cleaned_purchase_data.csv", index=False)
print("Cleaned file saved!")