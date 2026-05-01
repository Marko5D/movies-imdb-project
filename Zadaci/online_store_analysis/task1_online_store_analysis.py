import pandas as pd

# Ucitavanje CSV fajla
df = pd.read_csv("online_store_data.csv")

# Prikaz prvih 5 (da proverimo da li radi)
print(df.head())

# Ukupan broj proizvoda
print("\nUkupan broj proizvoda:", df.shape[0])