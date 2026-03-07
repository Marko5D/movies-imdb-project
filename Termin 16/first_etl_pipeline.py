import pandas as pd

df = pd.read_excel('users_rentals_v2.xlsx')

today = pd.Timestamp.today()
interval = today - df.loc(1, 'rental_date')

print(interval.days > 31)