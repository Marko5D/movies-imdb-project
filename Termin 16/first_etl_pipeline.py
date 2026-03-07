import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

for i in range(df.shape[0]):
    value = df.loc[i, 'total_rentals']
    print(i, type(value).__name__, value)