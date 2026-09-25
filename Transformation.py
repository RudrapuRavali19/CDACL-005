
import pandas as pd
df = pd.read_csv("cleaned_purchase_data.csv")
basket = df.groupby(['TransactionID', 'Product'])['Quantity'].sum().unstack().fillna(0)
basket_encoded = (basket > 0).astype(int)
print("BEFORE:", df.shape)
print("AFTER:", basket_encoded.shape)
print(basket_encoded.head())
basket_encoded.to_csv("basket_for_apriori.csv")
print("Transformed file saved!")