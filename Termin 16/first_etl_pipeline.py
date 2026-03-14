import pandas as pd

#extract
def extract_data(file_name):
    return pd.read_excel(file_name, engine='openpyxl')

#clean
def clean_data(df):
    for i in range(df.shape[0]):
        value = df.loc[i, 'rental_date']

        if(type(value).__name__ != 'datetime' and not(pd.isna(value))):

            df.loc[i, 'rental_date'] = pd.to_datetime(value, format='%d.%m.%Y', errors='raise')

    df['rental_date'] = pd.to_datetime(df['rental_date'], errors='raise')
    return df

#filter data
def filter_data(df):
    mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
    return df [mask]

#sort data
def sort_data(df):
    return df.sort_values(by='rental_date', ascending=True)
    
#add new column
def add_new_column(df):
    df['overdue_days'] = (pd.Timestamp.today() - df['rental_date']).dt.days - 31 
    return df

#remove columns
def remove_columns(df):
    return df.drop(columns=['address', 'gender', 'city', 'active']) 

#load data
def load_data(df):
    df.to_excel('overdue_users.xlsx', index=False)
    return df

df = extract_data('users_rentals_v2.xlsx').pipe(clean_data).pipe(filter_data).pipe(sort_data).pipe(add_new_column).pipe(remove_columns).pipe(load_data)