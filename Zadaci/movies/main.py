import pandas as pd

df = pd.read_csv("DMSP4-Task_02-movies.csv")

df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")

usa_df = df[df["country"].str.contains("USA", na=False)].copy()

usa_df["balance"] = usa_df["box_office"] - usa_df["budget"]

print(usa_df.head())