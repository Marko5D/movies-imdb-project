import pandas as pd

df = pd.read_csv('books.csv', index_col='id')

print(df.loc[103, 'title'])