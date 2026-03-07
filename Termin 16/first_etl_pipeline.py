import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

df['total_rentals'] = pd.to_numeric(df['total_rentals'], errors='coerce')

print(df.dtypes)