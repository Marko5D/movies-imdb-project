import pandas as pd

df = pd.read_csv("DMSP4-Task_02-movies.csv")

usa_df = df[df["country"].str.contains("USA", na=False)]

print(usa_df.head())

print(df.head())

print(df["country"].unique())