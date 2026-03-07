import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

df['total_rentals'] = df['total_rentals'].astype('float')

print(df.dtypes)