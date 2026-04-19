import pandas as pd

df = pd.read_csv("DMSP4-Task_02-movies.csv")

df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")

countries = ["USA", "Russia", "UK", "South Korea"]

for country in countries:

    temp_df = df[df["country"].str.contains(country, na=False)].copy()

    temp_df["balance"] = temp_df["box_office"] - temp_df["budget"]

    temp_df = temp_df.sort_values(by="balance", ascending=False)

    top10 = temp_df.head(10)

    top10 = top10[["title", "release_year", "genre", "director", "balance"]]

    top10.to_excel(f"top10_{country}.xlsx", index=False)

    print("Zavrseno za {country}")