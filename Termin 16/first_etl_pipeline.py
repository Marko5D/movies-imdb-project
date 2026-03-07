import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

for i in range(df.shape[0]):
    value = df.loc[i, 'rental_date']

    if(type(value).__name__ != 'datetime' and not(pd.isna(value))):

        df.loc[i, 'rental_date'] = pd.to_datetime(value, format='%d.%m.%Y', errors='raise')

df['rental_date'] = pd.to_datetime(df['rental_date'], errors='raise')

print(df.dtypes)

today = pd.Timestamp.today()
interval = today - df.loc[1, 'rental_date']

print(interval > pd.Timedelta(days=31))

      