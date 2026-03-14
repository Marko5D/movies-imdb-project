import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx', engine='openpyxl')

for i in range(df.shape[0]):
    value = df.loc[i, 'rental_date']

    if(type(value).__name__ != 'datetime' and not(pd.isna(value))):

        df.loc[i, 'rental_date'] = pd.to_datetime(value, format='%d.%m.%Y', errors='raise')

df['rental_date'] = pd.to_datetime(df['rental_date'], errors='raise')


mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]


new_df.sort_values(by='rental_date')


print(new_df)

      