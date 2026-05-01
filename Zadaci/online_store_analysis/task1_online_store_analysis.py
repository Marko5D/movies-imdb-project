import pandas as pd

# Ucitavanje CSV fajla
df = pd.read_csv("online_store_data.csv")

# Prikaz prvih 5 (da proverimo da li radi)
print(df.head())

# 1. Ukupan broj proizvoda
print("\nUkupan broj proizvoda:", df.shape[0])

# 2. Najprodavaniji proizvod
najprodavaniji = df.sort_values(by="quantity_sold", ascending=False).iloc[0]

print("\nNajprodavaniji proizvod:")
print(najprodavaniji)

# 3. Top 5 mobilnih telefona
smartphones = df[df["category"] == "Smartphones"]

top5_phones = smartphones.sort_values(by="quantity_sold", ascending=False).head(5)

print("\nTop 5 mobilnih telefona:")
print(top5_phones)