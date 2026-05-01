import pandas as pd

# Ucitavanje podataka
def load_data(file_path):
    """ Ucitava CSV fajl i vraca DataFrame. """
    df = pd.read_csv(file_path)
    return df


# Mere centralne tendencije

def analyze_product_rating(df):
    """ Racuna osnovne mere centralne tendencije za ocene proizvoda. """
    average_rating = df["rating"].mean()
    median_rating = df["rating"].median()
    mode_rating = df["rating"].mode()

    print("\n1. Prosecna ocena proizvoda u online trgovini")
    print("Aritmeticka sredina:", average_rating)
    print("Medijana:", median_rating)
    print("Mod:", mode_rating)

def analyze_most_common_brand(df):
    """ Pronalazi najcesci brend u online trgovini. """
    most_common_brand = df["brand"].mode()[0]

    print("\n2. Najcesci brend u online trgovini")
    print(most_common_brand)