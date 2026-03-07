import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

df['rental_date'] = pd.to_datetime(df['rental_date'], errors='raise')

print(df.dtypes)