import pandas as pd

df = pd.read_csv("DMSP4-Task_02-movies.csv")

df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")

usa_df = df[df["country"].str.contains("USA", na=False)].copy()

usa_df["balance"] = usa_df["box_office"] - usa_df["budget"]

usa_df = usa_df.sort_values(by="balance", ascending=False)

top10_usa = usa_df.head(10)

top10_usa = top10_usa[["title", "release_year", "genre", "director", "balance"]]

top10_usa.to_excel("top10_USA.xlsx", index=False)

print(usa_df.head())